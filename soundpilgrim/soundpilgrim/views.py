from django.shortcuts import render

def home(request):
    context = {'is_home': True}
    return render(request, 'index.html', context)
