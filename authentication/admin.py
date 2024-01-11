from django.contrib import admin

from authentication.models import  User

# Register your models here.

@admin.register(User)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("username",)

