from django.test import TestCase
from maths.models import Math, Result

class MathModelTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="add", a=1, b=2)
        Math.objects.create(operation="sub", a=20, b=30)

    def test_math_str(self):
        m1 = Math.objects.get(operation="add")
        m2 = Math.objects.get(operation="sub")

        expected_m1_str = f"id:{m1.id}, a={m1.a}, b={m1.b}, op={m1.operation}, result={m1.result}"
        expected_m2_str = f"id:{m2.id}, a={m2.a}, b={m2.b}, op={m2.operation}, result={m2.result}"

        # Dodatkowy warunek sprawdzający operację
        self.assertEqual(m1.operation, "add")

        self.assertEqual(str(m1), expected_m1_str)
        self.assertEqual(str(m2), expected_m2_str)

class ResultModelTest(TestCase):

    def test_result_str(self):
        # Tworzymy obiekt Result z wartością None dla atrybutu value
        r = Result.objects.create(error="0 division error!")  # Zmiana: Usunięcie value=None

        # Sprawdzamy, czy implementacja __str__ zwraca oczekiwaną wartość
        self.assertEqual(str(r), f'value: {r.value} | error: {r.error}')