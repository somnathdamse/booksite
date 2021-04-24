from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from booksite.models import Contact, myuploadfile
from django.contrib import messages
import psycopg2
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
     context={
          "variable":"Sent a variable",
          "var2":"How is that",
     }
     return render(request, 'index.html', context)

# def loginprocess(request):
#      first_name = request.POST['uname']
#      password = request.POST['psw']
#      # pass
#      return render(request, 'index.html')

def contact(request):
     return render(request, 'contact.html')
     # return redirect('contact.html',foo="bar")
        
def contactprocess(request):
     if request.method == "POST":
          name = request.POST["name"] 
          email = request.POST["email"]
          phone = request.POST["phone"] 
          desc  = request.POST["desc"] 
          dates  = datetime.today()     
          
          if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
               
               value = {
                    "name":name,
                    "email":email,
                    "phone":phone,
                    "desc":desc
               }
               messages.error(request, 'Please fill the form correctly')
               # value.append()
               return render(request, 'contact.html', value)
               
          else:    
               contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
               contact.save() 
               messages.success(request, 'Thank you for getting in touch !!!')

          # booksite_contact = Contact( name=name, email=email, phone=phone, desc=desc, date=dates )
          # booksite_contact.save()       
     return redirect("/contact")
    
     # return render(request, 'contact.html')

def about(request):
     som = {
          "d":"am",
          "b":"som",
     }
     return render(request, 'about.html', som)

# def login(request):
#      return render(request, 'login.html')

def upload(request):

     
     if request.method == "POST":

          file_pdf = request.FILES["uploadfile"] 
          # print(file_pdf.ext)
          file_name= request.POST["bookname"]
          description  = request.POST["desc"]      
          if file_name is "":
               print("erroe")
          else:
               fs = FileSystemStorage()
               document = myuploadfile(file=file_pdf, description=description, file_name=file_name)
               document.save()
               files = file_pdf

               upload_file_url = fs.url(files)
               messages.success(request, 'Thank you for building this library !!!')       
               return render(request, 'upload.html',{
                    "upload_file_url" : upload_file_url
               })


          # document.save() 
          # print(" after save document")

          # print(document)

     return render(request, 'upload.html')    
      
def search(request):
     query=request.GET['query']
     print(query)
     # allpost=myuploadfile.objects.all()
     allpost=myuploadfile.objects.filter(file_name__icontains=query)
     para={'allpost':allpost}
     return render(request,"search.html", para)
     # print(request.GET['search'])
     
     # if request.method == 'GET':
     #        book_name = request.GET['search'] # write your form name here      
     #      #   print (book_name )
     #        try:
     #            status = myuploadfile.objects.filter(description__icontains='book_name')
     #            print (status)
  
     #            return render(request,"search.html",{"books":status})
     #        except:
     #            return render(request,"search.html")

     #      #   book_name =  request.GET.get('myform')      
     #      #   try:
     #      #       status = myuploadfile.objects.filter(file=book_name)
     #      #       return render(request,"search.html",{"books":status})
     #      #   except:
     #      #       return render(request,"search.html",{'books':status})
     # else:
     #     print("book not found")
     #     return render(request, 'search.html', {'books':status})
     #     print ("book found")
     #     return render(request,"search.html")

def signup(request):
             return render(request,"signup.html")


# def search(request):        
#     if request.method == '"GET"':      
#         book_name =  request.POST.getlist('search')      
#         try:
#             status = Add_prod.objects.filter(bookname__icontains=book_name)
#             #Add_prod class contains a column called 'bookname'
#         except Add_prod.DoesNotExist:
#             status = None
#         return render(request,"search.html",{"books":status})
#     else:
#         return render(request,"search.html",{})




