from django.urls import path
from . import views

app_name = 'backgroundremover_frontend'

urlpatterns = [
    path('', views.index, name='index'),
]
