# Django libraries for requests, responses, file uploads, and CSRF
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

# Standard libraries
import os
import json
import torch
import collections
import nltk
import uuid
import traceback
import re
import numpy as np
import pandas as pd

from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm

# Ensures NLTK stuff are downloaded
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('average_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# JSON file to store history
HISTORY_FILE = ("history.json")

# Sentiment analyzer class
class SentimentAnalyzer:
   def __init__(self, model_name):
      # Load a pre-trained BERT model and tokenizer
      self.model_name = model_name
      self.tokenizer = AutoTokenizer.from_pretrained(model_name)
      self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
      self.model.eval()

   def predict(self, text):
      # Tokenize and prepare input
      inputs = self.tokenizer(text,
                              return_tensors='pt',
                              truncation = True,
                              padding = True,
                              max_length = 512,
                              is_split_into_words=False)
      
      # Disable gradient computation
      with torch.no_grad():
               outputs = self.model(**inputs)
               prediction = torch.argmax(outputs.logits, dim = 1).item()
      
      return prediction

# Upload dataset
@csrf_exempt
def upload_dataset(request):
   if request.method == 'POST' and request.FILES.get('file'):
      file = request.FILES['file']
      file_name = file.name # Ensures file is defined
      file_path = default_storage.save(file_name, file)

      # Verify file name reception
      if os.path.exists(default_storage.path(file_path)): # Checks for correct file
         return JsonResponse({'message': 'File uploaded successfully', 'file_path': file_path})
      else:
         return JsonResponse({'error': 'File upload failed'}, status = 400)
      
   return JsonResponse({'error': 'Invalid request'}, status = 400)

# Predefined analyzers
analyzers = {
   "Social Media": SentimentAnalyzer("finiteautomata/bertweet-base-sentiment-analysis"),
   "Customer Reviews": SentimentAnalyzer("nlptown/bert-base-multilingual-uncased-sentiment"),
   "Education": SentimentAnalyzer("bert-base-uncased"),
   "Fiction": SentimentAnalyzer("distilbert-base-uncased")
}

# # Analyze sentiment through training and testing
@csrf_exempt
def analyze_sentiment_deux(request):
   if request.method == 'POST':
      try:
         data = json.loads(request.body)
         texts = pd.DataFrame(data.get('texts', [])) # Expect text and sentiment array

         if not data:
            return JsonResponse({'error': 'No text provided'}, status = 400)
         
         # Initialize result containers
         sentiments = []
         predictions = []
         sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
         all_words = []
         result_id = str(uuid.uuid4())
         
         # Filter stop words, and texts
         stop_words = set(stopwords.words('english'))
         texts['text'] = texts['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
         texts['text'] = texts['text'].apply(lambda x: x.lower())
         texts['text'] = texts['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))

         # Train test split
         train_set, test_set = np.split(texts, [int(.8*len(texts))])

         # Count feature vectors
         vectorizer = TfidfVectorizer(min_df = 5,
                                      max_df = 0.8,
                                      sublinear_tf=True,
                                      use_idf=True)
         trainVectors = vectorizer.fit_transform(train_set['text'])
         testVectors = vectorizer.transform(test_set['text'])
         
         # Train and predict
         classifier = svm.SVC(kernel="linear")
         classifier.fit(trainVectors, train_set['sentiment'])
         prediction = classifier.predict(testVectors)

         for _, row in texts.iterrows():
            text_vector = vectorizer.transform([row['text']])
            label = classifier.predict(text_vector)[0]

            if label == "positive":
               sentiment = "positive"
            elif label == "negative":
               sentiment = "negative"
            else:
               sentiment = "neutral"
               
            sentiments.append({"text": row['text'], "sentiment": sentiment})
            predictions.append(label)
            sentiment_counts[sentiment] = sentiment_counts[sentiment] + 1

            # Tagging for word cloud
            tokens = word_tokenize(row['text'])
            tagged_words = pos_tag(tokens)

            # Keep adjectives, nouns and interjections
            allowed_tags = {'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'UH'}

            # Process words for word cloud
            filtered_words = [
               re.sub(r'[^\w\s]', '', word.lower())
               for word, tag in tagged_words
               if tag in allowed_tags
               and word.lower() not in stopwords.words("english")
               and len(re.sub(r'[^\w\s]', '', word)) > 1
            ]
            all_words.extend(filtered_words)
         
         # Process the performance metrics
         true_labels = test_set['sentiment']
         precision = precision_score(true_labels, prediction, average = "macro", zero_division = 0)
         recall = recall_score(true_labels, prediction, average = "macro", zero_division = 0)
         f1 = f1_score(true_labels, prediction, average = "macro", zero_division = 0)

         # Process word cloud frequencies
         word_freq = collections.Counter(all_words)
         top_words = word_freq.most_common(data.get("word_cloud", 20))
         max_count = top_words[0][1] if top_words else 1
         normalized_words = [{"word": word, "count": count / max_count * 100} for word, count in top_words]

         # Build history entry
         history_entry = {
            "id": result_id, # Assigns unique history ID
            "date": datetime.now().isoformat(), # Will replace with actual time
            "process": data.get("process", "None"),
            "dataset": data.get("dataset_name", "Unnamed Dataset"),
            "domain": data.get("domain_select", "None"),
            "show_only": data.get("show_only", "None"),
            "sentiments": sentiments,
            "sentiment_counts": sentiment_counts,
            "performance": {"precision": precision, "recall": recall, "f1_score": f1},
            "word_cloud": normalized_words
         }

         save_history(history_entry)

         return JsonResponse(history_entry)

      except Exception as exp:
         print("Exception Traceback: ")
         traceback.print_exc()
         return JsonResponse({'error': str(exp)}, status = 500)
         
   return JsonResponse({'error': 'Invalid request'}, status = 400)

# Analyze sentiment using pre-trained models
@csrf_exempt
def analyze_sentiment(request):
   if request.method == 'POST':
      try:
         data = json.loads(request.body)
         texts = data.get('texts') # Expects text array
         
         if not texts:
            return JsonResponse({'error': 'No text provided'}, status = 400)
         
         # Determines selected model based on domain
         if data.get("domain_select", "None") == "Social media":
            model = data.get('model', 'Social Media')
            analyzer = analyzers[model]
         elif data.get("domain_select", "None") == "Reviews":
            model = data.get('model', 'Customer Reviews')
            analyzer = analyzers[model]
         elif data.get("domain_select", "None") == "Education/News":
            model = data.get('model', 'Education')
            analyzer = analyzers[model]
         elif data.get("domain_select", "None") == "Fiction":
            model = data.get('model', 'Fiction')
            analyzer = analyzers[model]
         
         if model not in analyzers:
            return JsonResponse({'error': 'Invalid model'}, status = 400) # Throws invalid model error
         
         # Initialize result containers
         sentiments = []
         predictions = []
         sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
         all_words = []
         result_id = str(uuid.uuid4())

         # Perform predictions for each input
         for text in texts:
            prediction = analyzer.predict(text)
         
            # Map predictions with selected label
            if prediction == 2:
               sentiment = 'positive'
            elif prediction == 0:
               sentiment = 'negative'
            else:
               sentiment = 'neutral'

            sentiments.append({"text": text, "sentiment": sentiment})
            predictions.append(prediction)
            sentiment_counts[sentiment] = sentiment_counts[sentiment] + 1

            # Tokenize and tag POS
            tokens = word_tokenize(text)
            tagged_words = pos_tag(tokens)

            # Keep adjectives, nouns and interjections
            allowed_tags = {'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'UH'}

            # Process words for word cloud
            filtered_words = [
               re.sub(r'[^\w\s]', '', word.lower())
               for word, tag in tagged_words
               if tag in allowed_tags
               and word.lower() not in stopwords.words("english")
               and len(re.sub(r'[^\w\s]', '', word)) > 1
            ]
            all_words.extend(filtered_words)

         # Process the performance metrics
         precision = precision_score(predictions, [1] * len(predictions), average = "macro", zero_division = 0)
         recall = recall_score(predictions, [1] * len(predictions), average = "macro", zero_division = 0)
         f1 = f1_score(predictions, [1] * len(predictions), average = "macro", zero_division = 0)
         
         # Process word cloud frequencies
         word_freq = collections.Counter(all_words)
         top_words = word_freq.most_common(data.get("word_cloud", 20))
         max_count = top_words[0][1] if top_words else 1
         normalized_words = [{"word": word, "count": count / max_count * 100} for word, count in top_words]

         # Build history entry
         history_entry = {
            "id": result_id, # Assigns unique history ID
            "date": datetime.now().isoformat(), # Will replace with actual time
            "process": data.get("process", "None"),
            "dataset": data.get("dataset_name", "Unnamed Dataset"),
            "domain": data.get("domain_select", "None"),
            "show_only": data.get("show_only", "None"),
            "sentiments": sentiments,
            "sentiment_counts": sentiment_counts,
            "performance": {"precision": precision, "recall": recall, "f1_score": f1},
            "word_cloud": normalized_words
         }

         save_history(history_entry)

         return JsonResponse(history_entry)
      
      except Exception as exp:
         print("Exception Traceback: ")
         traceback.print_exc()
         return JsonResponse({'error': str(exp)}, status = 500)
      
   return JsonResponse({'error': 'Invalid request'}, status = 400)

# Save analysis history
def save_history(entry):
   # Save history entry into a file
   try:
      if os.path.exists(HISTORY_FILE):
         with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
      else:
         history = []

      history.append(entry) # Append entry and overwrite file

      with open(HISTORY_FILE, "w") as file:
         json.dump(history, file, indent = 4)

   except Exception as exp:
      print("Exception Traceback: ")
      traceback.print_exc()
      print(f"Error saving history: {exp}")

# Fetch history
@csrf_exempt
def get_history(request, entry_id = None):
   # Returns the saved analysis history
   try:
      if not os.path.exists(HISTORY_FILE):
         return JsonResponse({"error": "No history found."}, status = 404)
      
      with open(HISTORY_FILE, "r") as file:
         history = json.load(file)

      if entry_id:
         # Filter for specific history entry
         entry = next((h for h in history if h["id"] == entry_id), None)

         if entry:
            return JsonResponse(entry)
         else:
            return JsonResponse({"error": "History entry not found"}, status = 404)
         
      return JsonResponse({"history": history})

   except Exception as exp:
      print("Exception Traceback: ")
      traceback.print_exc()
      return JsonResponse({"error": str(exp)}, status = 500)

# Fetch specific history
@csrf_exempt
def get_history_entry(request, entry_id):
   # Fetches specific history entry
   if os.path.exists(HISTORY_FILE):
      with open(HISTORY_FILE, "r") as file:
         history = json.load(file)

      # Find the entry with the given ID
      entry = next((item for item in history if item["id"] == entry_id), None)

      if entry:
         return JsonResponse(entry)
      else:
         return JsonResponse({"error": "History entry not found."}, status = 404)

   return JsonResponse({"error": "History not found"}, status = 404)

# Deletes history entry
@csrf_exempt
def delete_history_entry(request, entry_id):
   # Deletes a specific history id
   try:
      if os.path.exists(HISTORY_FILE):
         with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

         # Filter out the entry given by ID
         history = [entry for entry in history if entry["id"] != entry_id]

         # Save updated history
         with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent = 4)

         return JsonResponse({"message": "History deleted."})
      
      return JsonResponse({"message": "History file not found."})
   
   except Exception as exp:
      print("Exception Traceback: ")
      traceback.print_exc()
      return JsonResponse({"error": str(exp)}, status = 500)

# Deletes all history entries
@csrf_exempt
def clear_all_history(request):
   # Deletes all history entries
   try:
      with open(HISTORY_FILE, 'w') as file:
         json.dump([], file, indent = 4)
      
      return JsonResponse({"message": "All history cleared."})
   
   except Exception as exp:
      print("Exception Traceback: ")
      traceback.print_exc()
      return JsonResponse({"error": str(exp)}, status = 500)