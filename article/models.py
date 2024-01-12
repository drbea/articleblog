from django.conf import settings
from django.db import models
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
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null = True)
    content = models.CharField(max_length = 5000, verbose_name = "Description")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    price = models.IntegerField(default = 0)
    devise = models.CharField(max_length = 5, null = True)
    panier = models.ForeignKey("article.Panier", on_delete=models.DO_NOTHING, null = True)
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
    
    pamier_name = models.CharField(max_length = 128, null = True)
    panier_user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.pamier_name
    