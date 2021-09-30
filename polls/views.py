from django.shortcuts import redirect, render , HttpResponse
from polls.models import Choice, Questions

# when we hit the url 127.0.0.1:8000/polls/  it should show the questions list

def index(request):
    #to get all the questions
    questions = Questions.objects.all();
    context = {'questions':questions}
    return render(request,"polls/index.html",context)

def details(request,question_id):
    question = Questions.objects.get(id=question_id)
    context = {'question':question}
    return render(request,"polls/details.html",context)

def vote(request,question_id):
    #taking choice_id from input tag
    choice_id = request.POST['choice']
    #get that specific question
    question = Questions.objects.get(id=question_id)
    #get that specific choice for the above question
    choice = question.choice_set.get(id=choice_id)
    choice.vote = choice.vote+1
    choice.save()
    return HttpResponse("Vote casted successfully")

def result(request,question_id):
    question = Questions.objects.get(id=question_id)
    #get all the choices for that question
    choice = question.choice_set.all()
    context = {'choices':choice}
    return render(request,"polls/result.html",context)