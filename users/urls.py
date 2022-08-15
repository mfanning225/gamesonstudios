from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit-account/', views.editAccount, name="edit-account"),

    path('register/', views.registerUser, name='register'),

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('countries/', views.countries, name='countries'),
    path('cities/', views.cities, name='cities'),


]
