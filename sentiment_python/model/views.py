from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

import os
import json
import torch
import collections
import nltk
import uuid

from nltk.corpus import stopwords
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.metrics import precision_score, recall_score, f1_score
from datetime import datetime

# Ensures NLTK stopwords are downloaded
nltk.download('stopwords')

HISTORY_FILE = ("history.json")

# Load a pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels = 2)
model.eval()

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

@csrf_exempt
def analyze_sentiment(request):
   if request.method == 'POST':
      try:
         data = json.loads(request.body)
         texts = data.get('texts') # Expects text array
         if not texts:
            return JsonResponse({'error': 'No text provided'}, status = 400)
         
         sentiments = []
         predictions = []
         sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
         all_words = []
         result_id = str(uuid.uuid4())

         for text in texts:
            inputs = tokenizer(text,
                            return_tensors='pt',
                            truncation = True,
                            padding = True,
                            max_length = 512)
            
            with torch.no_grad():
               outputs = model(**inputs)
               prediction = torch.argmax(outputs.logits, dim = 1).item()
         
            if prediction == 1:
               sentiment = 'positive'
            elif prediction == -1:
               sentiment = 'negative'
            else:
               sentiment = 'neutral'

            sentiments.append({"text": text, "sentiment": sentiment})
            predictions.append(prediction)
            sentiment_counts[sentiment] = sentiment_counts[sentiment] + 1

            # Process words for word cloud
            words = [word.lower() for word in text.split() if word.lower() not in stopwords.words("english")]
            all_words.extend(words)

         # Process the performance metrics
         try:
            precision = precision_score(predictions, [1] * len(predictions), average = "binary", zero_division = 0)
            recall = recall_score(predictions, [1] * len(predictions), average = "binary", zero_division = 0)
            f1 = f1_score(predictions, [1] * len(predictions), average = "binary", zero_division = 0)
         except Exception:
            precision, recall, f1 = 0, 0, 0 # Fallback values
         
         # Process word cloud frequencies
         word_freq = collections.Counter(all_words)
         top_words = word_freq.most_common(20)

         history_entry = {
            "id": result_id, # Assigns unique history ID
            "date": datetime.now().isoformat(), # Will replace with actual time
            "dataset": data.get("dataset", "Unknown"),
            "domain": data.get("domain_select", "None"),
            "sort_by": data.get("sort_by", "None"),
            "word_cloud": data.get("word_cloud", 20)
         }

         save_history(history_entry)

         return JsonResponse({
            "id": result_id,
            "sentiments": sentiments,
            "sentiment_counts": sentiment_counts,
            "performance": {"precision": precision, "recall": recall, "f1_score": f1},
            "word_cloud": [{"word": word, "count": count} for word, count in top_words]
         })
      
      except Exception as exp:
         return JsonResponse({'error': str(exp)}, status = 500)
      
   return JsonResponse({'error': 'Invalid request'}, status = 400)

def save_history(entry):
   # Save history entry into a file
   try:
      if os.path.exists(HISTORY_FILE):
         with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
      else:
         history = []

      history.append(entry)

      with open(HISTORY_FILE, "w") as file:
         json.dump(history, file, indent = 4)

   except Exception as exp:
      print(f"Error saving history: {exp}")

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
      return JsonResponse({"error": str(exp)}, status = 500)

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
      return JsonResponse({"error": str(exp)}, status = 500)
   
@csrf_exempt
def clear_all_history(request):
   # Deletes all history entries
   try:
      if os.path.exists(HISTORY_FILE):
         os.remove(HISTORY_FILE)
      
      return JsonResponse({"message": "All history cleared."})
   
   except Exception as exp:
      return JsonResponse({"error": str(exp)}, status = 500)