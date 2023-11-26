from django import forms
from captcha.fields import CaptchaField

from bang.models import Feedback


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
