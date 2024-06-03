from django.shortcuts import render


def Holistic_Insight(request):
    context = {}
    context['hello_Django'] = 'Hello Django!'
    return render(request, 'index.html', context)