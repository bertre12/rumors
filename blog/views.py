from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Реализация клиентских запросов.

# Реализация через функции.

# Отображение статей по дате создания.
def blog(request):
    articl = News.objects.order_by('-date')
    return render(request, 'blog/blog_about.html', {'articl': articl})


# Отображение страницы для создания статьи.
def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            error = 'Неправильно заполнено'

    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'blog/create.html', data)


# Реализация через классы.

# Переход на всю страницу.
class BlogDetailView(DetailView):
    model = News
    template_name = 'blog/details_view.html'
    context_object_name = 'article'


# Редактирование.
class BlogUpdatelView(UpdateView):
    model = News
    template_name = 'blog/create.html'
    form_class = NewsForm


# Удаление.
class BlogDeletelView(DeleteView):
    model = News
    success_url = '/blog/'
    template_name = 'blog/blog_delete.html'
