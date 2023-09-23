from django.urls import path
from . import views

# Создание перенаправленных url адресов.
urlpatterns = [
    path('', views.blog, name='blog'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update', views.BlogUpdatelView.as_view(), name='blog_update'),
    path('<int:pk>/delete', views.BlogDeletelView.as_view(), name='blog_delete')
]
