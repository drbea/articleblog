from django.conf import settings
from django.db import models
from PIL import Image


# Create your models here.

class Photo(models.Model):
    image = models.ImageField()
    #uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null= True, blank = True)
    #date_created = models.DateTimeField(auto_now_add = True)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)
    
    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        self.resize_image()

class Article(models.Model):

    title = models.CharField(max_length = 128)
    #photo = models.ForeignKey("Photo", on_delete = models.CASCADE)
    image = models.ImageField(default = None, null = True)
    content = models.CharField(max_length = 5000, verbose_name = "Description")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    #starred = models.BooleanField(default = False, null = True, verbose_name = "votes etoiles")
    price = models.IntegerField(default = 0)
    devise = models.CharField(max_length = 5, null = True)
    #date_created = models.DateTimeField(auto_now_add = True, null = True)
    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()