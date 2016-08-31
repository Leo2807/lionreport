from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import ugettext_lazy as _

from lionschool.core.models import Pupil, Teacher, Warden, Course


class Evaluation(models.Model):
    """This class represents an evaluation held. Not to be confused with the
    individual results of said evaluation, represented as :model: `Result`

    Attributes:
        title -- The title
        desc -- The description
        date -- When this evaluation was held/due
        course -- The course this evaluation belongs to
        public -- Wether the evaluation should be public
        """
    course = models.ForeignKey(Course, verbose_name=_("course"),
                               blank=True, null=True)
    title = models.CharField(_("title"), max_length=150)
    desc = models.TextField(_("description"), blank=True, null=True)
    date = models.DateField(_("date"))
    public = models.BooleanField(_("public"), default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = _("evaluation")
        verbose_name_plural = _("evaluations")


class Result(models.Model):
    """This class represents the individual results of a student, the overall
    evaluation is stored in Evaluation"""
    evaluation = models.ForeignKey(
        Evaluation, verbose_name=_("evaluation"), on_delete=models.CASCADE
    )
    score = models.PositiveIntegerField(
        verbose_name=_("score"), blank=True, null=True,
        validators=[MaxValueValidator(100)]
    )
    comment = models.TextField(_("comment"), blank=True, null=True)
    pupil = models.ForeignKey(Pupil, verbose_name=_("pupil"))

    class Meta:
        verbose_name = _('result')
        verbose_name_plural = _('results')

    def failed(self):
        return self.score < 50

    def __str__(self):
        return str(self.evaluation)
