from django import forms
from .models import *


class ApplyForm(forms.ModelForm):
    class Meta:
        model  = Cv_Reader
        fields = ['name', 'email', 'website', 'upload_cv', 'letter']


class JobForm(forms.ModelForm):
    class Meta:
        model  = Job
        fields = '__all__'
        exclude = ('slug','owner')