from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('thank-you', views.thankyou, name='thank-you'),

]
