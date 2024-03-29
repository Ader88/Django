from django.test import TestCase
from django.urls import reverse

class GreetViewWhitespaceNameTestCase(TestCase):
    def test_greet_with_whitespace_name(self):
        # Przygotowanie
        name = '    '
        expected_response = "Hello World!"

        # Wywołanie widoku greet z parametrem name zawierającym tylko spacje
        response = self.client.get(reverse('greet', kwargs={'name': name}))

        # Sprawdzenie czy otrzymana odpowiedź jest zgodna z oczekiwaną
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_response)