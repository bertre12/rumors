from django.shortcuts import render


# Реализация клиентских запросов.
def about(request):
    menu = {'title': 'Главная'}
    return render(request, 'main/about.html', menu)


def source(request):
    return render(request, 'main/source.html')
