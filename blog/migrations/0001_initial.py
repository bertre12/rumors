# Generated by Django 4.2.5 on 2023-09-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('article', models.TextField(verbose_name='Статья')),
                ('author', models.CharField(max_length=20, verbose_name='Автор')),
                ('date', models.DateField(verbose_name='Дата создания')),
            ],
        ),
    ]
