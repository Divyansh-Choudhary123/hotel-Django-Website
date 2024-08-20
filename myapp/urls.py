from django.urls import path
from.import views

urlpatterns = [
   path('',views.Home,name='Home'),
   path('loginData',views.loginData,name='loginData'),
   path('calanderData',views.calanderData,name='calanderData')
]