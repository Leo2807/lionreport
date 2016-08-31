from django.contrib import admin

from .models import Evaluation, Result

for model in Evaluation, Result:
    admin.site.register(model)
