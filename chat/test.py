from django.test import TestCase, Client
from django.urls import reverse
from django.test import TestCase
from chat.models import Message

class MessageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos iniciales para las pruebas
        Message.objects.create(sender='user1', content='Test message')

    def test_sender_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('sender').verbose_name
        self.assertEquals(field_label, 'sender')

    def test_content_label(self):
        message = Message.objects.get(id=1)
        field_label = message._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

class ChatViewsTest(TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/home.html')

    # Agrega más pruebas según sea necesario
