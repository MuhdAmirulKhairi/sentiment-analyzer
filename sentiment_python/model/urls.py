from django.urls import path
from .views import analyze_sentiment, upload_dataset, get_history

urlpatterns = [
   path("analyze_sentiment/", analyze_sentiment, name="analyze_sentiment"),
   path("upload_dataset/", upload_dataset, name="upload_dataset"),
   path("get_history/", get_history, name="get_history"),
]