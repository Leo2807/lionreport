from django.test import TestCase

from .models import Evaluation, Result


class EvaluationTest(TestCase):
    def test_correct_string_representation(self):
        title = "dfghjkdsf&&é"
        evaluation = Evaluation(title=title)
        self.assertEqual(title, str(evaluation))


class ResultTest(TestCase):
    def test_correct_string_representation(self):
        title = "dfghjkdsf&&é"
        evaluation = Evaluation(title=title)
        result = Result(evaluation=evaluation)
        self.assertEqual(title, str(result))

    def test_succeed_when_score_over_50(self):
        score = 75
        result = Result(score=score)
        self.assertIs(
            False, result.failed(),
            "Result isn't succeeded when score is {}".format(score)
        )

    def test_fail_when_score_under_50(self):
        score = 25
        result = Result(score=score)
        self.assertIs(
            True, result.failed(),
            "Result isn't failed when score is {}".format(score)
        )

    def test_succeed_when_score_fifty(self):
        score = 50
        result = Result(score=score)
        self.assertIs(
            False, result.failed(),
            "Result isn't succeeded when score is {}".format(score)
        )
