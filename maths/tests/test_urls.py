from django.test import TestCase
from django.urls import reverse, resolve
from maths.views import add, sub, mul, div, add_result
from django.urls.exceptions import NoReverseMatch

class TestUrls(TestCase):

    def test_resolution_for_add(self):
        url = reverse('add', args=[1, 2])
        resolver = resolve(url)
        self.assertEqual(resolver.func, add)

    def test_resolution_for_sub(self):
        url = reverse('sub', args=[1, 2])
        resolver = resolve(url)
        self.assertEqual(resolver.func, sub)

    def test_resolution_for_mul(self):
        url = reverse('mul', args=[1, 2])
        resolver = resolve(url)
        self.assertEqual(resolver.func, mul)

    def test_resolution_for_div(self):
        url = reverse('div', args=[1, 2])
        resolver = resolve(url)
        self.assertEqual(resolver.func, div)

    def test_resolution_for_add_result(self):
        url = reverse('add_result_url')
        resolver = resolve(url)
        self.assertEqual(resolver.func, add_result)

    def test_arguments_should_be_integers_or_404(self):
        # Sprawdź czy wywołanie reverse z niepoprawnymi argumentami raises NoReverseMatch
        with self.assertRaises(NoReverseMatch):
            reverse('add', args=['a', 'b'])

        # Sprawdź również czy wywołanie reverse z poprawnymi argumentami nie raises NoReverseMatch
        try:
            reverse('add', args=['1', '2'])
        except NoReverseMatch:
            self.fail("NoReverseMatch unexpectedly raised for valid arguments")