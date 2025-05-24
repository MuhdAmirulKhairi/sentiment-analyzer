from django.urls import path
from .views import analyze_sentiment_BERT, analyze_sentiment_train, analyze_sentiment_test, upload_dataset, get_history, get_history_entry, delete_history_entry, clear_all_history

urlpatterns = [
   path("analyze_sentiment_BERT/", analyze_sentiment_BERT, name="analyze_sentiment_BERT"),
   path("analyze_sentiment_train/", analyze_sentiment_train, name="analyze_sentiment_train"),
   path("analyze_sentiment_test/", analyze_sentiment_test, name="analyze_sentiment_test"),
   path("upload_dataset/", upload_dataset, name="upload_dataset"),
   path("get_history/", get_history, name="get_history"),
   path("get_history/<str:entry_id>", get_history_entry, name="get_history_entry"),
   path("delete_history/<str:entry_id>", delete_history_entry, name="delete_history_entry"),
   path("clear_all_history", clear_all_history, name="clear_all_history")
]