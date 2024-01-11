from django.shortcuts import render

from article.models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    searched_articles = ""
    if "search" in request.GET and request.GET["search"]:
        searched_query = request.GET.get("search")
        searched_articles = Article.objects.filter(title__contains = searched_query)
        
    context = {
        "articles": articles,
        "searched_articles": searched_articles,
        }

    return render(request, "blog/index.html", context)



def contact_us(request):
    context = {"form": "formulaire"}
    return render(request, "blog/contact_us.html", context)


def about_us(request):
    context = {"form": "formulaire"}
    return render(request, "blog/about_us.html", context)


def newsletters(request):
    context = {"form": "formulaire"}
    return render(request, "blog/newsletters.html", context)
