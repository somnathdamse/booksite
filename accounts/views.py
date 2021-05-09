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
        valid = {
        'valid_firstname':'',
        'valid_lastname':'',
        'valid_username':'',
        'valid_email':'',
        'valid_password':''
        }
        print(valid['valid_lastname'])            

        if first_name.isspace():
            valid["valid_firstname"] = '*** FIRST NAME NOT ENTERED'
            print(valid['valid_firstname'])            
            
                #  messages.info(request, "Check the form again")
                #  return render(request, 'signup.html',valid) 
        if last_name.isspace() :
                 valid["valid_lastname"] = '*** LAST NAME NOT ENTERED'
                 print(valid['valid_lastname'])              
                #  messages.info(request, "Check the form again")
                #  return render(request, 'signup.html',valid)
                 
        if username.isspace() :
                 valid_username='*** username NOT ENTERED'              
                 valid["valid_username"] = '*** USER NAME NOT ENTERED'
                 print(valid['valid_username'])            
                #  messages.info(request, "Check the form again")
                #  return render(request, 'signup.html',valid) 
        if email.isspace() :
                 valid_email='*** email NOT ENTERED'              
                 valid["valid_email"] = '*** USER NAME NOT ENTERED'
                 print(valid['valid_email']) 
                             
                #  messages.info(request, "Check the form again")
                #  return render(request, 'signup.html',valid) 

        if password.isspace() :
                 valid_password='*** password NOT ENTERED'              
                             
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
                    return render(request, 'signin.html')     
         
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
        # user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = "please enter valid login Id and Password"
            return render(request, 'signin.html', {"username":username,"password":password,"message":message})
    else:
        return render(request, 'signin.html')    
          
    
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