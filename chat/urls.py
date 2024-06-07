# chat/urls.py

from django.urls import path
from .views import UserCreateView, MessageListView, ChatRoomView

urlpatterns = [
    path('chat/<str:room_name>/', ChatRoomView.as_view(), name='chat_room'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('messages/', MessageListView.as_view(), name='messages'),
]
