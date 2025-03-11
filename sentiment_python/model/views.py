from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

import os
import json
import torch
import collections
import nltk

from nltk.corpus import stopwords
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.metrics import precision_score, recall_score, f1_score

# Ensures NLTK stopwords are downloaded
nltk.download('stopwords')

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
         precision = precision_score(predictions, [1] * len(predictions), average = "binary", zero_division = 0)
         recall = recall_score(predictions, [1] * len(predictions), average = "binary", zero_division = 0)
         f1 = f1_score(predictions, [1] * len(predictions), average = "binary", zero_division = 0)
         
         # Process word cloud frequencies
         word_freq = collections.Counter(all_words)
         top_words = word_freq.most_common(20)

         return JsonResponse({
            "sentiments": sentiments,
            "sentiment_counts": sentiment_counts,
            "performance": {"precision": precision, "recall": recall, "f1_score": f1},
            "word_cloud": [{"word": word, "count": count} for word, count in top_words]
         })
      
      except Exception as exp:
         return JsonResponse({'error': str(exp)}, status = 500)
      
   return JsonResponse({'error': 'Invalid request'}, status = 400)