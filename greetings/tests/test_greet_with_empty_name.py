# Plik: test_greet_empty_name.py

from django.test import TestCase
from django.urls import reverse

class GreetViewEmptyNameTestCase(TestCase):
    def test_greet_with_empty_name(self):
        # Przygotowanie
        name = ''
        expected_response = "Hello World!"

        # Wywołanie widoku greet z pustym parametrem name
        response = self.client.get(reverse('greet', kwargs={'name': name}))

        # Sprawdzenie czy otrzymana odpowiedź jest zgodna z oczekiwaną
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_response)