from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, Quote, Favorite

# Create your views here.

def index(request):
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        user_id= request.session['id']
        fav_id=Favorite.objects.order_by('quote_id')



        context ={
            'quotes': Quote.objects.all().order_by('-id'),
            'favs': Favorite.objects.filter(user_id= user_id).order_by('-id'),
            # 'filters': Favorite.objects.exclude(id__in = [Favorite['quote_id'] for Favorite in Quote])

        }



        return render(request, 'beltapp/index.html', context)

def create(request):
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        quote_create = Quote.objects.create_quote(request.POST)
        print quote_create,"<----"

        if quote_create[0] == False:
            for error in quote_create[1]:
                messages.error(request, error)
                return redirect('belt:index')
        else:
            return redirect('belt:index')



def remove_quote(request, id):

    print "removes quote"
    # quote_del = Quote.objects.get(id=id)
    # print quote_del
    # quote_del.delete()
    return HttpResponse("Deleted")

def add(request,id):
    if 'id' not in request.session:
        return redirect ('login:index')
    else:
        favorite = Favorite.objects.add_favorite(request.POST)

        print favorite[2].quote_id, "<----- favorite manager"
        print favorite[2].quote_id, "what is quote"

        Quote.objects.get(id = favorite[2].quote_id).delete()
        # print favorite[2].user.id
        # # print favorite[2].fav_quoter
        # # print favorite[2].fav_message
        #
        # fav = Favorite.objects.create(
        # user_id = favorite[2].user.id,
        # fav_quoter = favorite[2].fav_quoter,
        # fav_message = favorite[2].fav_message,
        # )
        if favorite[0] == True:
            # print fav,
            return redirect ('belt:index')



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
    readd= Quote.objects.readd_quote(request.POST)

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
