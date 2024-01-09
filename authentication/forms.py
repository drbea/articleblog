#from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from authentication.models import User


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name", "birth_date", "phone_number")
        #exclude = ("profile_pick", "friends",)  


class LoginForm(forms.Form):
    #email = forms.EmailField(label = "Email")
    username = forms.CharField(max_length= 50, required=True)
    password = forms.CharField(label= "Password", max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        # verifie si les deux champs sont valide
        if email and password:
            result = User.objects.filter(password = password, email = email)
            if len(result) != 1:
                raise forms.ValidationError("adresse de couriel ou mot de passe invalide!!!")
        return cleaned_data



class AddFriendForm(forms.Form):
    email = forms.EmailField(label="Couriels")
    def clean(self):
        clean_data = super(AddFriendForm, self).clean()
        email = clean_data.get("email")
        # verifie si le champ est valide
        if email:
            result = User.objects.filter(email= email)
            if len(result) != 1:
                raise forms.ValidationError("Adress couriel non valide!")
        return clean_data


 