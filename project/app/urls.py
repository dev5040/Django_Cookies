

from django.urls import path
#from .views import home,about,contact,search,register,login,savedata, logindata
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('register/',register,name='register'),
    path('savedata/',savedata,name='savedata'),
    path('login/',login,name='login'),
    path("logindata/", logindata, name="logindata"),
    path("logout/", logout, name="logout")
    
    
]