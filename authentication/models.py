from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    profile_pick = models.ImageField(verbose_name = "Photo de profil", null=True)
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length = 20, default = None, null=True)
    #friends = models.ManyToManyField("self", null=True)


#class Person(AbstractUser):
#   #registration_number = models.CharField(max_length = 10)
#    last_name = models.CharField(max_length = 50)
#    first_name = models.CharField(max_length = 50)
#    username = models.CharField(max_length = 50, unique = True)
#    birth_date = models.DateField()
#    email = models.EmailField(max_length=254, unique = True)
#    phone_number = models.CharField(max_length = 20)
#    # Dans un cas reel nous ne devrions pas stocker le mode pass en clair
#    #password = models.CharField(max_length = 32)
#    friends = models.ManyToManyField("self")
#    #person_type = 'generic'
#    profile_pick = models.ImageField(verbose_name = "Photo de profil", default = None, null = True)



