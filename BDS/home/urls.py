from django.urls import path
from . import views #create functionality

#URL CONFIGURATION MODULE
urlpatterns = [
    path('', views.home, name='home'),#All urls followed by "home/" will display the HTML specified in our Views
    path('login/', views.loginPage, name='loginPage'),
    path('register/', views.registerPage, name='registerPage'),
]