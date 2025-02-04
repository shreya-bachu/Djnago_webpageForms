from django import forms
from app.models import *

def check_for_k(value):
    if value.lower()[0]=='k':
        raise forms.ValidationError('Name is Started with k')

def check_for_len(value):
    if len(value)<=5:
        raise forms.ValidationError('len is < 5')

class TopicForm(forms.Form):
    topic_name=forms.CharField(validators=[check_for_k,check_for_len])

class TopicModelForm(forms.ModelForm):
    class Meta:
        model=topic
        fields='__all__'

class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()
    reemail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot has catched')

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('emails are not matched')


class WebpageModelForm(forms.ModelForm):
    reemail=forms.EmailField()
    bot=forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model=webpage
        fields='__all__'
    
    def clean_bot(self):
        bott=self.cleaned_data['bot']
        if len(bott)>0:
            raise forms.ValidationError('bot has catched')

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('emails are not matched')


        
        
        
        
        
        
        #fields=['topic_name','name','url']
        #exclude=['email']
        #labels={'name':'WebpageName'}
        #widgets={'topic_name':forms.RadioSelect}
        #help_texts={'topic_name':'THis Is Belongs To PT'}


