from.views import *
from django.urls import path

urlpatterns=[
    path('home/',home,name='home'),
    path('products/',products,name='products'),
    path('addproduct/',addproduct,name='addproduct'),
    path('team/',team,name='team'),
    path('addteam/',addteam,name='addteam'),
]