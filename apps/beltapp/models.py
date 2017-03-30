from __future__ import unicode_literals

from django.db import models
from ..loginapp.models import User
from django.contrib.sessions.backends.db import SessionStore


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
            return (True, flash, quote)

    def readd_quote(self, data):
        flash=[]
        quote = self.create(
        quoter = data['quoter'],
        message = data['message'],
        user_id = data['user_id']
        )
        return (True, flash, quote)


    # pass

class FavoriteManager(models.Manager):
    def add_favorite(self, data):
        flash=[]

        quote = Favorite.objects.create(
        quote_id = data['quote'],
        user_id = data['uid'],
        fav_quoter = data['quoter'],
        fav_message = data['message'],
        )
        print "test"



        return (True, flash, quote)

        pass



class Quote(models.Model):

    quoter = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()
    def __unicode__(self):
        return unicode(self.id)+" "+self.quoter+" "+self.message

class Favorite(models.Model):
    fav_quoter = models.CharField(max_length=255)
    fav_message = models.TextField()
    quote_id = models.IntegerField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FavoriteManager()
    def __unicode__(self):
        return unicode(self.id)+" "+self.quote_id+" "+self.fav_quoter+" "+self.fav_message+" "+unicode(self.user)
