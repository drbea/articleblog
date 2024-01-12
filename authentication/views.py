from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from article.models import Panier

from . import forms

# Create your views here.
def logout_user(request):
    logout(request)
    return render(request, "authentication/logout.html")

class LoginPageView(View):
    template_name = "authentication/login.html"
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(request, self.template_name, context = { "form": form, "message": message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("blog:home")
                message = f"bonjour, {user.username} vous etes connecte"
            else:
                message = "Identifiants invalides !!!"
        
        return render(request, self.template_name, context = { "form": form, "message": message})

def login_page(request):

    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("blog:home")
                message = f"bonjour, {user.username} vous etes connecte"
            else:
                message = "Identifiants invalides !!!"

    context = { "form": form,
               "message": message}
    return render(request, "authentication/login.html", context)

    
def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    context = {
        "form": form
    }
    return render(request, "authentication/signup.html", context)


def about_us(request):

    return render(request, "authentication/about_us.html")


def contact_us(request):
    context = { "form": "form"}
    return render(request, "authentication/contact_us.html", context)


def user_account(request):
    context = { "form": "form"}
    return render(request, "authentication/user_account.html", context)


def user_panier(request):

    panier = None
    if request.user != "":
        panier = Panier.objects.filter(panier_user = request.user) 
    context = { "panier": panier}
    return render(request, "authentication/user_panier.html", context)

    