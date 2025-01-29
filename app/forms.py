from django import forms
from app.models import *
class TopicForm(forms.Form):
    tname=forms.CharField()

class WebForm(forms.Form):
    tname=forms.ModelChoiceField(queryset=topic.objects.all())
    name=forms.CharField()
    email=forms.EmailField
    url=forms.URLField()



