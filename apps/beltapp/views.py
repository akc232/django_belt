from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, Quote, Favorite

# Create your views here.

def index(request):
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        user_id= request.session['id']
        context ={
            'quotes': Quote.objects.all().order_by('-id'),
            'favs': Favorite.objects.filter(user_id= user_id),

        }
        print context


        return render(request, 'beltapp/index.html', context)

def create(request):
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        quote_create = Quote.objects.create_quote(request.POST)

        if quote_create[0] == False:
            for error in quote_create[1]:
                messages.error(request, error)
                return redirect('belt:index')
        else:
            return redirect('belt:index')

def add(request,id):
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        favorite = Quote.objects.fav_quote(request.POST)

        if favorite[0] == True:
            
            return redirect('belt:index')

def show(request, id):
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        context={
            'quotes': Quote.objects.filter(user_id=id),
            'counts': Quote.objects.filter(user_id=id).count(),
        }


        return render (request, 'beltapp/user.html', context)

def destroy(request,id):
    delete = Favorite.objects.get(id=id)
    delete.delete()


    return redirect(reverse('belt:index'))


















# index: Display all products
# show: Display a particular product
# new: Display a form to create a new product
# edit: Display a form to update a product
# create: Process information to create a new product
# update: Process information from the edit form and update the particular product
# destroy: Remove a product
