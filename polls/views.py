from urllib import request
from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import RequestContext
from django.shortcuts import  loader, get_object_or_404
from django.core.urlresolvers import reverse

def index(request):
    # return HttpResponse("Hello world, you're at the polls index.")

    # latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question do not exist")
    # return render(request, "polls/index.html", {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    # p.question_text = request.POST['choice']
    # return render(request, 'polls/detail.html', {'question': p})

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


