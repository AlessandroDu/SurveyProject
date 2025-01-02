from django import forms
from .models import Question, Option


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'question']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['optionText']
