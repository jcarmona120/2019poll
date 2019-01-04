from django.http import HttpResponse
from .models import Question, Choice
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse
import json
from textblob import TextBlob

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

        feelings = data.decode("utf-8")
        sentimentObj = json.loads(feelings)
        neg = sentimentObj['probability']['neg']
        pos = sentimentObj['probability']['pos']
        neutral = sentimentObj['probability']['neutral']

        sentiment = 'neutral'

        b = TextBlob(text)
        print(b.sentiment)
        print(b.noun_phrases)

        if neutral > (pos and neg):
            print('neutral')
            sentiment = 'neutral'
        elif pos > (neg and neutral):
            print('pos')
            sentiment = 'positive'
        else:
            print('neg')
            sentiment = 'negative'

        context = {
            "probability": sentimentObj['probability'],
            "label": sentimentObj['label'],
            "sentiment": sentiment
        }

        return render(request, 'feelingsApp/detail.html', context)

    return render(request, 'feelingsApp/detail.html')
