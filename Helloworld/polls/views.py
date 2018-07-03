from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Question
from django.template import loader
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name = 'polls/results.html'

# def index(request):
#     last_question_list=Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     # 字典key的名字要和html模板上的名字一样啊。
#     context = {'latest_question_list':last_question_list}
#     # output=','.join([q.question_text for q in last_question_list])
#     return HttpResponse(template.render(context,request))

# def detail(request,question_id):
#     # try:
#     #     question=Question.objects.get(pk=question_id)
#     # except Exception as e:
#     #     raise Http404('Question does not exist')
#
#     question=get_object_or_404(Question,pk=question_id)
#
#     return render(request,'polls/detail.html',{'question':question})
#     #return HttpResponse("you're looking at question %s" % question_id)

# def results(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})
#     # return HttpResponse('you are looking at the results of question %s' % question_id)


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except Exception as e:
        return render(request,'polls/detail.html',
                      {'question':question,
                      'error_message':'you didnt select a choice',})
    else:
        selected_choice.votes+=1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    # return HttpResponse('you are voting on question %s'%question_id)

