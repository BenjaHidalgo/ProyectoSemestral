from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('orden/', orden, name='orden'),
    path('login/', login, name='login'),

    
]