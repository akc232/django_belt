from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import datetime
# Create your views here.
def index(request):
    context={
    # 'data': User.objects.all(),
    }

    return render(request,'loginapp/index.html', context)

def process(request):
    process=User.objects.create_new_user(request.POST)
    print process, "process session"
    # print process


    if process[0] == False:
        print process[1]
        for error in process[1]:
            messages.error(request, error)
        return redirect ('login:index')

    else:
        messages.info(request, success)
        request.session['id']=process[2].id
        request.session['name']= process[2].first_name
        request.session['last']= process[2].last_name
        request.session['email']= process[2].email
        # print process

        return redirect('belt:index')

def login(request):

    result= User.objects.check_user(request.POST)
    print result," login session"
    print result[1].id


    if result[0] ==False:
        for error in result[1]:
            messages.error(request, error)
            return redirect('login:index')

    else:
        request.session['id']=result[1].id
        request.session['name']= result[1].first_name
        request.session['last']= result[1].last_name
        request.session['email']= result[1].email

        return redirect('belt:index')

def success(request):


    if 'id' not in request.session:

        return redirect('login:index')
    else:

        return render(request, 'belt:index')

def logout(request):
    request.session.clear()
    # print  "session"
    return redirect ('login:index')
