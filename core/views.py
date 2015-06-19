from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseBadRequest
from django.db import transaction
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Test, Question, UserQuestion


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

@ensure_csrf_cookie
def test(request, username, test_name):
    owner = get_object_or_404(User, username=username)
    test = get_object_or_404(Test, owner=owner, name=test_name)
    return render(request, 'test.html', {'test': test})

@require_POST
def save_active_questions(request):
    states = [t == 'true' for t in request.POST.getlist('states[]')]
    tokens = request.POST.get('test').split('/')
    if len(tokens) != 2:
        return HttpResponseBadRequest()
    owner_name, test_name = tokens

    owner = get_object_or_404(User, username=owner_name)
    test = get_object_or_404(Test, owner=owner, name=test_name)
    questions = test.question_set
    if questions.count() != len(states):
        return HttpResponse(status=409)

    with transaction.atomic():
        for question, is_active in zip(questions.all(), states):
            user_question, _ = UserQuestion.objects.get_or_create(
                user=owner,
                question=question
            )
            user_question.is_active = is_active
            user_question.save()

    return HttpResponse()
