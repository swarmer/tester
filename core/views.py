from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseBadRequest
from django.db import transaction
from django.core import exceptions


from .models import Test, Question, UserQuestion
from .forms import TestForm


def index_list(request):
    tests = Test.objects.filter(owner=request.user)
    return render(request, 'core/index_list.html', {'tests': tests})

def index_intro(request):
    return render(request, 'core/index_intro.html')

def index(request):
    if request.user.is_authenticated():
        return index_list(request)
    else:
        return index_intro(request)

def explore(request):
    public_tests = Test.objects.filter(is_listed=True)
    return render(request, 'core/explore.html', {'tests': public_tests})

@ensure_csrf_cookie
def test(request, username, test_name):
    owner = get_object_or_404(User, username=username)
    test = get_object_or_404(Test, owner=owner, name=test_name)

    questions = list(test.question_set.all())
    for question in questions:
        question.is_active = True

        if not request.user.is_authenticated():
            continue

        try:
            user_question = UserQuestion.objects.get(
                user=request.user,
                question=question
            )
            question.is_active = user_question.is_active
        except exceptions.ObjectDoesNotExist:
            pass

    return render(request, 'core/test.html', {
        'test': test,
        'questions': questions,
    })


class TestNew(CreateView):
    http_method_names = ['get', 'post', 'options']

    model = Test
    form_class = TestForm
    template_name = 'core/test_new.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TestEdit(UpdateView):
    http_method_names = ['get', 'post', 'options']

    model = Test
    form_class = TestForm
    template_name = 'core/test_edit.html'

    def get_queryset(self):
        return Test.objects.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()

        username, test_name = self.args
        owner = get_object_or_404(User, username=username)
        return get_object_or_404(queryset, owner=owner, name=test_name)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TestDelete(DeleteView):
    http_method_names = ['post', 'options']

    model = Test
    success_url = '/'

    def get_queryset(self):
        return Test.objects.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()

        username, test_name = self.args
        owner = get_object_or_404(User, username=username)
        return get_object_or_404(queryset, owner=owner, name=test_name)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@require_POST
def save_active_questions(request):
    if not request.user.is_authenticated():
        return HttpResponse()

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
                user=request.user,
                question=question
            )
            user_question.is_active = is_active
            user_question.save()

    return HttpResponse()
