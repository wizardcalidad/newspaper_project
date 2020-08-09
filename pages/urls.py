from django.urls import path, include
from .views import HomePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', HomePageView.as_view(), name = 'home'),
     #path('password_change/',auth_views.PasswordChangeView.as_view(), name = 'password_change'),

]

