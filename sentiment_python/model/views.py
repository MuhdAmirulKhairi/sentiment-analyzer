from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

import os
import json
import nltk
import torch

from transformers import BertTokenizer, BertForSequenceClassification

# Load a pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels = 2)
model.eval()

@csrf_exempt
def upload_dataset(request):
   if request.method == 'POST' and request.FILES.get('file'):
      file = request.FILES['file']
      file_name = default_storage.save(file_name, file)
      file_path = default_storage.path(file_name)

      # Verify file name reception
      if os.path.exists(file_path):
         return JsonResponse({'message': 'File uploaded successfully', 'file_path': file_path})
      else:
         return JsonResponse({'error': 'File upload failed'}, status = 400)
      
   return JsonResponse({'error': 'Invalid request'}, status = 400)

@csrf_exempt
def analyze_sentiment(request):
   if request.method == 'POST':
      try:
         data = json.loads(request.body)
         text = data.get('text')
         if not text:
            return JsonResponse({'error': 'No text provided'}, status = 400)
         
         # Tokenize and predict sentiment
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

         return JsonResponse({'sentiment': sentiment})
      
      except Exception as exp:
         return JsonResponse({'error': str(exp)}, status = 500)
      
   return JsonResponse({'error': 'Invalid request'}, status = 400)