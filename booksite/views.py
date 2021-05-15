from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from booksite.models import Contact, bookstore
from django.contrib import messages
import psycopg2
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
     
     allpost = bookstore.objects.all()
     # print(allpost)

     context = {
          'allpost': allpost
     }


     return render(request, 'index.html', context)

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
  
     return render(request, 'about.html')

# def login(request):
#      return render(request, 'login.html')

def upload(request):

     
     if request.method == "POST":

          file_pdf = request.FILES["uploadfile"] 
          # print(file_pdf.ext)
          file_name= request.POST["bookname"]
          file_imagex= request.FILES["imgfile"]
          description  = request.POST["desc"]      
          if  file_name.isspace() or description.isspace() :
                messages.error(request, 'File name or Description can not be empty !!!')       
                return render(request,'upload.html')

          else:
               fs = FileSystemStorage()
               
               document = bookstore(file=file_pdf, description=description, file_name=file_name, file_image=file_imagex)
               document.save()
               files = file_pdf
               file_images = file_imagex

               upload_file_url = fs.url(files)
               file_image_url = fs.url(file_images)
               messages.success(request, 'Thank you for building this library !!!')       
               return render(request, 'upload.html',{
                    "upload_file_url" : upload_file_url,
                    "file_image_url" : file_image_url
               })


          # document.save() 
          # print(" after save document")

          # print(document)

     return render(request, 'upload.html')    
      
def search(request):
     
     query=request.GET['query']
     # allpost=myuploadfile.objects.all()
     allpost=bookstore.objects.filter(file_name__icontains=query)
     para={ 'allpost':allpost, "lenght": len(allpost) }
     return render(request,"search.html", para)


def signup(request):
             return render(request,"signup.html")














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




