from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User, UserManager


class RegisterUserForm(UserCreationForm):
    is_agree = forms.BooleanField()
    class Meta(UserCreationForm):
      model = User
      fields = ('is_agree','first_name','last_name','username','email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
  username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Search your waste bank here!'}))
  password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input','placeholder': 'Search your waste bank here!'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Message', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))



