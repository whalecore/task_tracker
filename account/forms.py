from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField, DateTimeField, SplitDateTimeField
from django.forms.models import inlineformset_factory
from django.forms.widgets import SplitDateTimeWidget

from .models import Task, Subtask


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']


class TaskForm(forms.ModelForm):
    redline = DateTimeField(input_formats=['%H:%M, %d.%m.%Y'])
    deadline = DateTimeField(input_formats=['%H:%M, %d.%m.%Y'])

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['redline', 'deadline']


class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
