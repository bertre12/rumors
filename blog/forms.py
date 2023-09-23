from .models import News
from django.forms import ModelForm, TextInput, DateInput, Textarea


# Создание формы для заполнения записи.
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'article', 'author', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'article': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
        }
