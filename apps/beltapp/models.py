from __future__ import unicode_literals

from django.db import models
from ..loginapp.models import User

# Create your models here.


class QuoteManager(models.Manager):
    def create_quote(self, data):
        flash=[]

        if len(data['quoter'])< 3:
            flash.append('Must be more that 3 characters.')

        if len(data['message'])<10:
            flash.append('Mesage must be more than 10 characters.')
        if flash:
            return (False, flash)
        else:
            quote = self.create(
            quoter = data['quoter'],
            message = data['message'],
            user_id = data['user_id']
            )
            return (True, flash)

    def fav_quote(self,data):
        flash=[]
        quote = Favorite.objects.create(
        user_id = data['user'],
        quote_id = data['quote']
        )
        return (True, flash )

    # pass

class FavoriteManager(models.Manager):
    pass


class Quote(models.Model):

    quoter = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

class Favorite(models.Model):
    quote= models.ForeignKey(Quote)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FavoriteManager()
