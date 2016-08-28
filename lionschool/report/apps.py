from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
import os


class LionreportConfig(AppConfig):
    name = 'lionschool.report'
    label = 'lionreport'
    verbose_name = _("Reports")
    path = os.path.dirname(os.path.abspath(__file__))
