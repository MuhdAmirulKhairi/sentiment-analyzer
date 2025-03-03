import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

nltk.download('all') # Downloads all NLTK resources

@api_view(['POST'])
def analyze_sentiment(request):
   # Handles CSV uploads and sentiment analysis
   if 'file' not in request.FILES:
      return Response({"error": "No file uplaoded"}, status = 400)
   
   file = request.FILES['file']
   try:
      df = pd.read_csv(file) # Reads CSV
      if 'text' not in df.columns:
         return Response({"error": "No such text column"}, status = 400)
      
      sentiment_obj = SentimentIntensityAnalyzer()
      df['sentiment'] = df['text'].apply(lambda text: sentiment_obj.polarity_scores(str(text))['compound'])

      # Classify sentiment
      df['label'] = df['sentiment'].apply(lambda score: 'positive' if score > 0.05 else 'negative' if score < -0.05 else 'neutral')

      return JsonResponse(df[['text', 'label']].to_dict(orient = 'records'), safe = False)
   except Exception as exp:
      return Response({"error": str(exp)}, status = 500)