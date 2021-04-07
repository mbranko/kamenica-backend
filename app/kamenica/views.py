from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html', content_type='text/html')


def privacy(request, language):
    return render(request, template_name='privacy.html', context={'language': language}, content_type='text/html')
