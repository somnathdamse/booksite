from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from booksite.models import Contact
from django.contrib import messages
import psycopg2
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout




# from accounts.models import User

# Create your views here.

def signup(request):

    if request.method == "POST":
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1'] 
        valid_lastname=''
        valid_lastname=''
        valid_lastname=''
        if first_name.isspace():
        # and last_name.isspace() and username.isspace() and email.isspace() and password.isspace():
                 valid={'valid_firstname':'*** FIRST NAME NOT ENTERED'
                     
                  
                             }
                 messages.info(request, "Check the form again")
                 return render(request, 'signup.html',valid) 
        else:
                if password==password1:
                                        
                   if User.objects.filter( username=username ).exists():
                       messages.info(request, 'username taken')
                       return render(request, 'signup.html')   
                   elif User.objects.filter(email=email).exists(): 
                       messages.info(request, 'Email is taken')
                       return render(request, 'signup.html')     
                   else: 
                    user= User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password )
                    user.save()
                    messages.info(request, "User created bhai")
                    return render(request, 'signin.html',ab)     
         
                else:
                     messages.error(request, 'password not matching')
                     return render(request, 'signup.html')   
    else:
        print("User not created error hai")
        return render(request, 'signup.html')     

# def loginprocess(request):
#      if request.method == "POST":
#            username = request.POST['username']
#            password = request.POST['password']

#            user=auth.authenticate(username=username,password=password)
#            print('usernamebbbbbbbbbbb')
#            print(user.username)
#            if user is not None:
#                auth.loginprocess(request, user)
#                return redirect('')
#            else:
#                print('username not valiad')
#                return render(request, 'signin.html')

#      else:
#           print('username yyyyyy')
#           return render(request, 'index.html')          

        # user= User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password )
        # user.save()


def signin(request):
      if request.method == "POST":
           username = request.POST['username']
           password = request.POST['password']
           user = authenticate(request, username=username, password=password)
           print('usernamebbbbbbbbbbb')
           print(user.username)
        #    user=auth.authenticate(username=username,password=password)
           
           if user is not None:
               print('usernamebbbbbbbbbbb')
               login(request, user)
               print('usernamebbbbbbbbbbb')
               return redirect('/')
            #    auth.signin(request, user)
           else:
               print('username not valiad')
               return render(request, 'signin.html')

      else:
          print('username yyyyyy')
          return render(request, 'signin.html')    
          
    # return render(request, 'signin.html') 
    # if request.method == "POST":
    #    username = request.POST['username']
    #    password = request.POST['password']

    #    user=auth.authenticate(username=username, password=password)

    #    if user is not None:
    #        auth.signin(request, user)
    #        return redirect('/')    
    #    else:
    #       print('elae wala part')
        #   return redirect('signin')

        # user= User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password )
        # user.save()
def index(request):
     context={
          "variable":"Sent a variable",
          "var2":"How is that",
     }
     return render(request, 'index.html', context)

def Signout(request):
    print('hello bhai')
    logout(request)
    return redirect('/')
    # auth.Signout(request)
    # return render(request, 'index.html')
    # return render(request, 'index.html')























    
 

# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)

#     return conn


# if psw==psw.repeat:
         #     if User.objects.filter( username=username ).exists():
         #          print('username is taken')
         #     elif User.objects.filter(email=email).exists():   
         #         print('Email is taken')
         #     else: 
         #        user= User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=psw )
         #        user.save()
         #        print("User created bhai")
         #        return render(request, 'signup.html') 