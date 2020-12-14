from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponse
#from django.http import Registration
#from django.http import Login
#from .models import Destination

# Create your views here.

def index(request):
    return render(request,"home/index.html")




def register(request):

    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password1 = request.POST['password1']
       password2 = request.POST['password2']
#-----------------------------------------------------
       gender = request.POST['gender']
       doc_id = request.POST['doc_id']
       dept = request.POST['dept']
       hospital = request.POST['hospital']
       phone = request.POST['phone']
       print(username, password1, password2, email, first_name, last_name, doc_id, dept, hospital, phone,gender)
#---------------------------------------------------
       if password1==password2:
           if User.objects.filter(username=username).exists():
               #print('Username Taken')
               messages.info(request,'Username Taken')
               return redirect('register')
             #  return redirect('register')

           elif User.objects.filter(email=email).exists():
                 #print('Email Already Exists')
                 messages.info(request,'Email Already Exists')
                 return redirect('register')
           else:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name,
            doc_id=doc_id, dept=dept, hospital=hospital, phone=phone, gender=gender)
            user.save();
            print(' User Created')
            messages.info(request,'User Created')
            return redirect('login')

       else:
          #print('Passwords Not Matching')
          messages.info(request,'Passwords Not Matching')
          return redirect('register')
       return redirect('login')

    else:
          return render(request,'reg.html')



def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user=auth.authenticate(username=username, password=password)

       if user is not None:
           auth.login(request, user)
           return redirect('/home')
       else:
           messages.info(request,'invalid credentials')
           return redirect('login')

    else:
       return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/home')






from django.shortcuts import render

# Create your views here.
