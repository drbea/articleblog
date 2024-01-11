from django.contrib import admin

from article.models import Article, Panier, Photo

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",)

    # filtrer selon un certain nombre d'enregistrement
    #list_filter = ["shop"]
    #search_fields = ["articleName"]


    #ajouter de la pagination pour ne pas afficher tous les elements sur une seule page
    #list_per_page = 8

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("image",)
    
@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ("panier_user",)
