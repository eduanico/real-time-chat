# chat/views.py

from rest_framework import generics
from django.contrib.auth.models import User
from .models import Message
from .serializers import UserSerializer, MessageSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer
