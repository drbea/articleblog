from django.urls import path, include
from . import views

app_name = "article"

urlpatterns = [
    path("upload_article/", views.upload_article, name="upload_article"),
    path("<int:article_id>/detail/", views.article_details, name = "article_details"),
]
