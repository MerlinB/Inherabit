from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from dms.models import Controller

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # Additional Fields for Users?
    #testfield = forms.IntegerField(required=False)

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.controller = Controller(user=self.instance)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
