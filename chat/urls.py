# chat/urls.py

from django.urls import path
from .views import UserCreateView, MessageListView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('messages/', MessageListView.as_view(), name='messages'),
]
