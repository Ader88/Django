from django.test import TestCase
from django.urls import reverse

class GreetViewSpecialCharactersTestCase(TestCase):
    def test_greet_with_special_characters_name(self):
        # Przygotowanie
        name = 'John!@#'
        expected_response = f"Hello {name.capitalize()}!"

        # Wywołanie widoku greet z parametrem name zawierającym znaki specjalne
        response = self.client.get(reverse('greet', kwargs={'name': name}))

        # Sprawdzenie czy otrzymana odpowiedź jest zgodna z oczekiwaną
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_response)