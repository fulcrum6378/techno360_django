from django.shortcuts import render

CORE = 'core.html'


def index(request):
    return render(request, CORE, {'name': 'index', 'html': 'index.html'})


def library(request):
    return render(request, CORE, {'name': 'library', 'html': 'library.html'})


def lessons(request):
    return render(request, CORE, {'name': 'lessons', 'html': 'lessons.html'})
