from django.urls import path
from  . views import *

urlpatterns = [

path ('', Home, name='home'),
path ('create/', Create, name='create'),
path ('delete/<int:id>', delete, name='delete'),
path ('update/<int:id>',update, name='update'),
]
