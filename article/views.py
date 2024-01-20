from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from article.forms import ArticleForm
from article.models import Article, LinePanier, Panier
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


#@login_required
def add_to_panier(request, article_id):
    # Récupérer l'article à partir de l'ID
    article = Article.objects.get(id=article_id)

    # Vérifier si l'utilisateur a déjà un panier
    panier, created = Panier.objects.get_or_create(user=request.user)

    # Vérifier si l'article est déjà dans le panier
    ligne_panier, created = LinePanier.objects.get_or_create(panier=panier, article=article)

    # Si l'article est déjà dans le panier, augmenter la quantité
    if not created:
        ligne_panier.quantite += 1
        ligne_panier.save()
    else:
        # Sinon, créer une nouvelle ligne dans le panier
        LinePanier.objects.create(panier=panier, article=article, quantite=1)
    return redirect('liste_articles')  # Rediriger vers la page de la liste des articles ou une autre page selon votre structure

# @login_required
def ajouter_au_panier(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    panier, created = Panier.objects.get_or_create(user=request.user)
    ligne_panier, created = LinePanier.objects.get_or_create(panier=panier, article=article)
    if not created:
        ligne_panier.quantite += 1
        ligne_panier.save()

    return redirect('blog:home')

def show_panier(request):
    panier, created = Panier.objects.get_or_create(user=request.user)
    articles_dans_panier = panier.articles.all()

    context = {
        'panier': panier,
        'articles_dans_panier': articles_dans_panier,
        "unlog_message": "Vous n'etes pas identifie encore",
    }

    return render(request, 'article/user_panier.html', context)