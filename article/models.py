from django.conf import settings
from django.db import models
from django.db.models import Sum
from PIL import Image


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 128, default = "Category")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    

class Article(models.Model):

    title = models.CharField(max_length = 128, null = True)
    image = models.ImageField(default = None, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    content = models.CharField(max_length = 5000, verbose_name = "Description")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    #price = models.IntegerField(default = 0)
    price = models.DecimalField(max_digits= 10, decimal_places= 1)
    devise = models.CharField(max_length = 5, null = True)
    #date_created = models.DateTimeField(auto_now_add = True, null = True)
    #starred = models.BooleanField(default = False, null = True, verbose_name = "votes etoiles")

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return str(self.title) or ""

class Panier(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null= True)
    articles = models.ManyToManyField(Article, through= "LinePanier")

    def total(self):
        return self.articles.aggregate(Sum("price"))["price__sum"]

class LinePanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete= models.CASCADE)
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1) 