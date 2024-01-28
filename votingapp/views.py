from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
from django.http import Http404

# Create your views here.
#Getting questions and displaying them
def questions(request):
    latest_question_list = Question.object.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questions.html', context)

#Showing the questions and choices
def choices(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'choices.html', {'question': question})

#Getting questions and displaying results
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'results.html', {'question':question})

#Vote for a question option
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'choices.html', {'question': question, 'error_message':'You didnt select a choice'})
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question_id,)))