# chat/views.py
from django.views import View
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Message
from .serializers import UserSerializer, MessageSerializer
from django.shortcuts import render

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer

class ChatRoomView(View):
    def get(self, request, room_name):
        return render(request, 'chat/chat.html', {'room_name': room_name})