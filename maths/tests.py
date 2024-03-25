from django.test import TestCase
from maths.models import Math, Result

class MathModelTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="add", a=1, b=2)
        Math.objects.create(operation="sub", a=20, b=30)

    def test_math_str(self):
        m1 = Math.objects.get(operation="add")
        m2 = Math.objects.get(operation="sub")

        self.assertEqual(str(m1), "Math object (1)")
        self.assertEqual(str(m2), "Math object (2)")

class ResultModelTest(TestCase):

    def setUp(self):
        Result.objects.create(value=10)
        Result.objects.create(error="0 division error!")

    def test_result_str(self):
        r1 = Result.objects.get(value=10)
        r2 = Result.objects.get(error="0 division error!")

        self.assertEqual(str(r1), 'Result object (1)')
        self.assertEqual(str(r2), 'Result object (2)')
