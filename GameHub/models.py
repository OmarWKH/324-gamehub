from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    #email = models.EmailField(max_length=20, unique=True)
    country = CountryField()
    user = models.OneToOneField(User)


    def __unicode__(self):
        return self.email