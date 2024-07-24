from django.urls import path

from .views import ResultDetailView, ResultListCreateView, message_list_recieve

urlpatterns = [
    path("message/", ResultListCreateView.as_view(), name="message"),
    path("message/<int:pk>/", ResultDetailView.as_view(), name="message-detail"),
    path("messages/", message_list_recieve, name="messages")
]