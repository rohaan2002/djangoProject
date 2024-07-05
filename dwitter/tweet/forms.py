from django import forms
from .models import Tweet, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    # in class , passing something in means inheriting so here, TweetForm inheriting from forms.ModelForm
    
    # ek meta class deni hi rhti which tells ki Form konsa model use krra, along with konsi field chiye
    class Meta:
        model = Tweet
        fields = ["text", "photo"] #wahi fields derkhi array m joki Tweet model m likh rkhi
        

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ('username', 'email', 'password1', 'password2')
        # the fields of built-in model in django is specified in tuple