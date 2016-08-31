from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.utils import timezone

from lionschool.core.models import Course, Teacher

from .models import Evaluation, Result
from .admin import EvaluationAdmin


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


class TestEvaluationAdmin(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.superuser = User.objects.create_superuser(
            username="su", email="", password="pw"
        )
        self.suEvaluation = Evaluation(
            title="suEvaluation", date=timezone.now(),
        )
        self.suEvaluation.save()
        self.teacherUser = User.objects.create_user(
            username="teacher", email="", password="pw"
        )
        self.teacherUser.save()
        self.teacher = Teacher(user=self.teacherUser)
        self.teacher.save()
        self.teEvaluation = Evaluation(
            title="teEvaluation", date=timezone.now()
        )
        self.teCourse = Course(name="")
        self.teCourse.save()
        self.teCourse.teachers = (self.teacher,)
        self.teCourse.save()
        self.teEvaluation.course = self.teCourse
        self.teEvaluation.save()
        self.ea = EvaluationAdmin(Evaluation, None)

    def test_get_queryset_superuser(self):
        request = self.factory.get('/')
        request.user = self.superuser
        qs = self.ea.get_queryset(request)
        self.assertIn(self.suEvaluation, qs,
                      "superuser doesn't see all evaluations")
        self.assertIn(self.teEvaluation, qs,
                      "superuser doesn't see teacher evaluations")

    def test_get_queryset_teacher(self):
        request = self.factory.get('/')
        request.user = self.teacherUser
        qs = self.ea.get_queryset(request)
        self.assertIn(self.teEvaluation, qs,
                      "teacher doesn't see own evaluations")
        self.assertNotIn(self.suEvaluation, qs, "teacher sees all evaluations")
