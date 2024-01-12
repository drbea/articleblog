#from typing import Any
from django import forms

from article.models import Article



class ArticleForm(forms.ModelForm):
    #edit_article = forms.BooleanField(widget = forms.HiddenInput, initial = True)

    class Meta:
        model = Article
        exclude = ["author", "starred", "panier"]
