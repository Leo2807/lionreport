from django.contrib import admin
from django.forms import modelform_factory, Textarea, NumberInput
from lionschool.core.models import Course

from .models import Evaluation, Result


class ResultInline(admin.TabularInline):
    model = Result
    form = modelform_factory(
        model, fields=('score', 'comment', 'pupil'), widgets={
            'comment': Textarea(attrs={'cols': 80, 'rows': 1}),
            'score': NumberInput()
        }
    )


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    inlines = (ResultInline,)
    date_hierarchy = 'date'
    fields = (('course', 'title'), ('date', 'public'), 'desc')
    search_fields = ('title', 'desc', 'course__name')
    list_filter = ('course', 'public', 'date')
    list_display = ('course', 'title', 'date', 'public')

    def get_queryset(self, request):
        qs = super(EvaluationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        course = Course.objects.filter(teachers__user=request.user)
        return qs.filter(course=course)
