from django.shortcuts import render

from article.models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    searched_articles = ""
    if request.method == "POST":
        search = request.POST["search"]
        posts = Article.objects.filter(title__contains = search)

        return render(request, "blog/search_result.html", { "query": search, "posts": posts })

    context = {
        "articles": articles,
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
