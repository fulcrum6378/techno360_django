from django.shortcuts import render


def index(request):
    context = {'latest_question_list': None,}
    return render(request, 'core.html', context)
