from django import forms
from captcha.fields import CaptchaField

from bang.models import Feedback, Pay


# Feedback form
class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label='Имя', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Search your waste bank here!'}))
    email = forms.CharField(label='Почта', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Search your waste bank here!'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message', 'captcha')


class PayForm(forms.ModelForm):
    username = forms.CharField(label='Имя', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input', 'style': 'text-transform: uppercase;'}))
    phone_number = forms.CharField(initial='+7', label='Почта', max_length=12, widget=forms.TextInput(attrs={'pattern': '^[+]?[0-9]+$','title': 'Enter phone number (only numbers and + symbol are allowed)','class': 'form-input'}))
    address = forms.CharField(label='Сообщение', widget=forms.Textarea(
        attrs={'class': 'form-input', 'rows': 10,
               'style': 'resize:none;  border: 2px solid #B7B7B7;  border-radius: 8px; width: 530px; padding: 20px 20px; font-size: 16px;'}))
    code = forms.CharField(label='Имя', max_length=3, widget=forms.PasswordInput(
        attrs={'pattern': '[0-9]*','title': 'Please enter only digits','class': 'form-input','class': 'form-input'}))

    class Meta:
        model = Pay
        fields = ('username', 'address', 'phone_number')
