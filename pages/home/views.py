from django.shortcuts import render


def home(request):
    context = {

    }
    return render(request, 'home/index.html', context=context)
