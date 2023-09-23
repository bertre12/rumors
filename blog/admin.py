from django.contrib import admin
from .models import News

# Регистрация модели/таблицы в admin панели.
admin.site.register(News)
