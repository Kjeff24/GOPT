from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm

# inherit UserCreationForm to create SignupForm
class SignupForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input-text form-control",
                "autocomplete":"email",
                'id':"floatingInput",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "toggleable-password form-control",
                'id':"floatingInput1",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "toggleable-password form-control",
                'id':"floatingInput2",
            }
        )
    )
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        

# create a login form
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input-text form-control",
                "autocomplete":"email",
                'id':"floatingInput",
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "toggleable-password form-control",
                "autocomplete":"password",
                "placeholder": "Enter your password",
                "id":"floatingPassword",
            }
        )
    )

# User Form
class UserForm(ModelForm):
    """
    Form for updating user information.

    Provides fields for updating the user's first name, last name, username, bio, and avatar.
    """
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Retrieve the 'user' argument from kwargs
        super().__init__(*args, **kwargs)  