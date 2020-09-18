from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Listotvet, Listscore
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('id')
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
def vote(request, question_id):
    getquestion = get_object_or_404(Question, pk=question_id)
    try:
        getlistotvet = Listotvet(question=getquestion, otvet = "0")
        getlistscore = Listscore(otvet = getlistotvet, score = 0)

        selected_choice = request.POST['listotvet']
        getlistotvet.otvet = selected_choice
        getlistotvet.save()
        if (selected_choice == getquestion.question_answer):
            getlistscore.score = 1
        else:
            getlistscore.score = 0
        getlistscore.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/polls/')
    except:
        return HttpResponse("Вы уже отвечали на этот вопрос")

class ResultsView(generic.ListView):
    template_name = 'polls/results.html'
    context_object_name = 'listscore_list'
    def get_queryset(self):
        return Listscore.objects.order_by('id')
def reset(request):
    Listotvet.objects.all().delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/polls/')

