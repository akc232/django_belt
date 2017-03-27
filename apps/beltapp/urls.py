from django.conf.urls import url,include
from . import views

app_name = 'belt'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^add/(?P<id>\d+)$', views.add, name='add'),
    url(r'^user/(?P<id>\d+)$', views.show, name='user'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),



]










# (?P<id>\d+)$

# index: Display all products
# show: Display a particular product
# new: Display a form to create a new product
# edit: Display a form to update a product
# create: Process information to create a new product
# update: Process information from the edit form and update the particular product
# destroy: Remove a product
