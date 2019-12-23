from django.urls import path
from . import views

app_name = 'Entree'
urlpatterns = [
    path('', views.indexView, name='entree')
]