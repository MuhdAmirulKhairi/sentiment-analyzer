from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
import json
import pandas as pd
import io

nltk.download('all')

sentiment_obj = SentimentIntensityAnalyzer()

def analyze_sentiment(request):
   if request.method == "POST":
      try:
         if "file" in request.FILES:
            csv_file = request.FILES["file"]

            if not csv_file.name.endswith(".csv"):
               return JsonResponse({"error": "Only CSV files allowed."}, status = 400)

            df = pd.read_csv(io.StringIO(csv_file.read().decode("utf-8")))

            if "text" not in df.columns:
               return JsonResponse({"error": "CSV files must contain text data."}, status = 400)

            df["sentiment"] = df["text"].apply(lambda x: classify_sentiment(x))

            return JsonResponse({"results": df.to_dict(orient="records")}, safe = False)
         
         data = json.loads(request.body)
         text = data.get("text", "")

         if not text:
            return JsonResponse({"error": "No text provided."}, status = 400)

         sentiment = classify_sentiment(text)
         sentiment_score = sentiment_obj.polarity_scores(text)

         return JsonResponse({
            "text": text,
            "sentiment": sentiment,
            "score": sentiment_score
         })

      except Exception as exp:
         return JsonResponse({"error": str(exp)}, status = 500)

   return JsonResponse({"error": "Invalid request method."}, status = 405)

def classify_sentiment(text):
   score = sentiment_obj.polarity_scores(text)
   if score["compound"] >= 0.05:
      return "positive"
   elif score["compound"] <= -0.05:
      return "negative"
   else:
      return "neutral"