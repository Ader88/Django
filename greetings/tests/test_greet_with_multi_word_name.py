from django.test import TestCase
from django.urls import reverse

class GreetViewMultiWordTestCase(TestCase):
    def test_greet_with_multi_word_name(self):
        # Przygotowanie
        name = 'John Doe'
        expected_response = f"Hello {name.capitalize()}!"

        # Wywołanie widoku greet z parametrem name zawierającym więcej niż jedno słowo
        response = self.client.get(reverse('greet', kwargs={'name': name}))

        # Sprawdzenie czy otrzymana odpowiedź jest zgodna z oczekiwaną
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_response)
