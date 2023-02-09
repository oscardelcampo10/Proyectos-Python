from django.urls import  path, include

from apps.adopcion.views import index_adopcion

app_name= 'adopcion'

urlpatterns = [
    path('',index_adopcion, name='index_adopcion'),
]