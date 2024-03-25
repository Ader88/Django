from django.test import TestCase
from maths.forms import ResultForm
from maths.models import Result

class ResultFormTest(TestCase):

    def test_result_save_correct_data(self):
        data = {"value": 200, "error": "Testowa wiadomość"}
        self.assertEqual(len(Result.objects.all()), 0)
        form = ResultForm(data=data)
        self.assertFalse(form.is_valid())
        expected_error = "Podaj tylko jedną z wartości"
        self.assertIn(expected_error, form.errors["__all__"])
