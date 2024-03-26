from django.test import TestCase, Client
from maths.models import Math
from django.urls import reverse

class MathViewsTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        self.client = Client()

    def test_maths_list(self):
        response = self.client.get(reverse("maths_list_url"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
        math_entry = Math.objects.get(operation="sub", a=20, b=30)
        
        self.assertIn(f'id:{math_entry.id}, a={math_entry.a}, b={math_entry.b}, op={math_entry.operation}', response.content.decode())
