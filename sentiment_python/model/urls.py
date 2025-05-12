from django.urls import path
from .views import analyze_sentiment, analyze_sentiment_deux, upload_dataset, get_history, delete_history_entry, clear_all_history

urlpatterns = [
   path("analyze_sentiment/", analyze_sentiment, name="analyze_sentiment"),
   path("analyze_sentiment_deux/", analyze_sentiment_deux, name="analyze_sentiment_deux"),
   path("upload_dataset/", upload_dataset, name="upload_dataset"),
   path("get_history/", get_history, name="get_history"),
   path("get_history/<str:entry_id>", get_history, name="get_history_entry"),
   path("delete_history/<str:entry_id>", delete_history_entry, name="delete_history_entry"),
   path("clear_all_history", clear_all_history, name="clear_all_history")
]