from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
#from . import forms
from article.forms import ArticleForm, PhotoForm
from article.models import Article
# Create your views here.

def upload_article(request):
    article_form = ArticleForm(request.POST)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit = False)
            article.author = request.user
            #article.image = request.POST["image"]
            article.save()
            return redirect("blog:home")
        else:
            return HttpResponse("<h1>formulaire ivalide...</h1>")

    context = {
        "article_form": article_form,        
    }
    return render(request, "article/article_upload.html", context)

def article_details(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    context = {
        "article": article
    }
    return render(request, "article/article_details.html", context)