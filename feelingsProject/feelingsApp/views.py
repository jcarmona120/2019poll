from django.http import HttpResponse
from .models import Question, Choice
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.


def index(request):
    question = Question.objects.get(pk=1)
    output = question
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'feelingsApp/index.html', context)


def question_list(request):
    return HttpResponse("You're looking at a question")


def vote(request):
    question = Question.objects.get(pk=1)
    output = question
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'feelingsApp/detail.html', context)
