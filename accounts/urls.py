from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings 



urlpatterns = [
        path('admin/', admin.site.urls),
        # path('', views.index, name ='home'),
        path('signup', views.signup, name ='signup'),
        path('signin', views.signin, name ='signin'),
        path('Signout', views.Signout, name ='Signout')

]
        
        
        # path('loginprocess', views.loginprocess, name ='loginprocess')
