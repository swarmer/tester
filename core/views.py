from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Test


def index_list(request):
    tests = Test.objects.filter(owner=request.user)
    return render(request, 'index_list.html', {'tests': tests})

def index_intro(request):
    return render(request, 'index_intro.html')

def index(request):
    if request.user.is_authenticated():
        return index_list(request)
    else:
        return index_intro(request)

def explore(request):
    public_tests = Test.objects.filter(is_listed=True)
    return render(request, 'explore.html', {'tests': public_tests})

def test(request, username, test_name):
    owner = get_object_or_404(User, username=username)
    test = get_object_or_404(Test, owner=owner, name=test_name)
    return render(request, 'test.html', {'test': test})
