from django.urls import path, include
from . import views
from article import views as articleViews
app_name = "authentication"

urlpatterns = [
    path("login/", views.login_page, name = "login"),
    path("logout/", views.logout_user, name = "logout"),
    path("signup/", views.signup_page, name = "signup"),
    path("account", views.user_account, name = "user_account"),
]
