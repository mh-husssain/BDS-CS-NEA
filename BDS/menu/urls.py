from django.urls import path
from . import views #create functionality

#URL CONFIGURATION MODULE
urlpatterns = [
    path('', views.home),
    path('about-us', views.aboutUs),
    path('balance/', views.balance),
    path('econometrics', views.econometrics),
    path('logout', views.logoutPage)
]


