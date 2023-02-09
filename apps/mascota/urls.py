
from django.urls import  path, include

from apps.mascota.views import index

apps_name= 'mascota'

urlpatterns = [
    path('',index, name='index'),
]