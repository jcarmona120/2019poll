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
    if request.method == "POST":
        print(request.POST.get('text'))
        text = request.POST.get('text')

        import http.client

        conn = http.client.HTTPConnection("text-processing.com")

        payload = "text={}".format(text).encode('utf-8')
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'postman-token': "d7009e69-4162-2afa-df9c-15683ef75510"
        }

        conn.request("POST", "/api/sentiment/", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        context = {"nlp": data.decode("utf-8")}

        return render(request, 'feelingsApp/detail.html', context)

    return render(request, 'feelingsApp/detail.html')
