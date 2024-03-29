from django.test import TestCase, Client
from maths.models import Math
from django.urls import reverse

class MathViewsTestCase(TestCase):
    def test_add_view(self):
        # Utwórz obiekt testowy w bazie danych
        Math.objects.create(a=2, b=3, operation='add', result=5)

        # Utwórz adres URL dla widoku 'add' z parametrami a=2 i b=3
        url = reverse('add', kwargs={'a': 2, 'b': 3})

        # Wyślij żądanie GET pod ten adres URL
        response = self.client.get(url)

        # Sprawdź, czy kod statusu odpowiedzi wynosi 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Sprawdź, czy oczekiwana zawartość jest obecna w odpowiedzi
        self.assertContains(response, '2 + 3 = 5')

    def test_sub_view(self):
        # Utwórz obiekt testowy w bazie danych
        Math.objects.create(a=5, b=3, operation='sub', result=2)

        # Utwórz adres URL dla widoku 'sub' z parametrami a=5 i b=3
        url = reverse('sub', kwargs={'a': 5, 'b': 3})

        # Wyślij żądanie GET pod ten adres URL
        response = self.client.get(url)

        # Sprawdź, czy kod statusu odpowiedzi wynosi 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Sprawdź, czy oczekiwana zawartość jest obecna w odpowiedzi
        self.assertContains(response, '5 - 3 = 2')

    def test_mul_view(self):
        # Utwórz obiekt testowy w bazie danych
        Math.objects.create(a=4, b=6, operation='mul', result=24)

        # Utwórz adres URL dla widoku 'mul' z parametrami a=4 i b=6
        url = reverse('mul', kwargs={'a': 4, 'b': 6})

        # Wyślij żądanie GET pod ten adres URL
        response = self.client.get(url)

        # Sprawdź, czy kod statusu odpowiedzi wynosi 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Sprawdź, czy oczekiwana zawartość jest obecna w odpowiedzi
        self.assertContains(response, '4 * 6 = 24')

    def test_div_view(self):
        # Utwórz obiekt testowy w bazie danych
        Math.objects.create(a=12, b=4, operation='div', result=3)

        # Utwórz adres URL dla widoku 'div' z parametrami a=12 i b=4
        url = reverse('div', kwargs={'a': 12, 'b': 4})

        # Wyślij żądanie GET pod ten adres URL
        response = self.client.get(url)

        # Sprawdź, czy kod statusu odpowiedzi wynosi 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Sprawdź, czy oczekiwana zawartość jest obecna w odpowiedzi
        self.assertContains(response, '12 / 4 = 3')