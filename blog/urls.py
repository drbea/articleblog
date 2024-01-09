from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name = "home"),
    path("about_us/", views.about_us, name = "about_us"),
    path("contact/", views.contact_us, name = "contact_us"),
    path("newsletters/", views.newsletters, name = "newsletters"),
]
