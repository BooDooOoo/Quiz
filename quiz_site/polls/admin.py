from django.contrib import admin
from django import forms
from .models import *


class PollsAdminForm(forms.ModelForm):
    class Meta:
        model = Polls
        fields = '__all__'


class PollsAdmin(admin.ModelAdmin):
    form = PollsAdminForm
    list_display = ('id', 'title', 'description', 'date_start', 'date_stop')
    fields = ('title', 'description', 'date_start', 'date_stop')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('date_start',)

        return self.readonly_fields


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ('id', 'text', 'type_question', 'polls')


class ChoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'


class ChoiceAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ('id', 'text', 'questions')


# Регистрация в админке модели Reminders и вывод полей
admin.site.register(Polls, PollsAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
