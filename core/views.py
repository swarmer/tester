from django.shortcuts import render

from .models import Test


def index(request):
    return render(request, 'index.html')

def explore(request):
    public_tests = Test.objects.filter(is_public=True)
    return render(request, 'explore.html', {'tests': public_tests})
