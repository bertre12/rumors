from django.db import models


# Создание модели/таблицы в бд и для просмотра в admin панели.
class News(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name='Название')
    anons = models.CharField(max_length=250, null=False, verbose_name='Анонс')
    article = models.TextField(null=False, verbose_name='Статья')
    author = models.CharField(max_length=20, null=False, verbose_name='Автор')
    date = models.DateField(null=False, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
