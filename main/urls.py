from django.urls import path
from . import views

# Создание перенаправленных url адресов.
urlpatterns = [
    path('', views.about, name='about'),
    path('source/', views.source, name='source'),
]