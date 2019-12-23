from django.shortcuts import render
from .models import Question, Choice
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# obtien les questions et les affiches
@login_required(login_url='/comptes/login/')
def indexView(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'indexvote.html', context)


# montrer les questions et les choix pour chaque question
@login_required(login_url='/comptes/login/')
def detailView(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("La question n'existe pas")
    return render(request, 'detail.html', {'question': question})


# obtien les questions et montre le resultat
@login_required(login_url='/comptes/login/')
def resultView(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

@login_required(login_url='/comptes/login/')
def voteView(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # reenvoie toutes les questions données
        return render(request, 'detail.html', {
                'question': question,
                'error_message': "Vous n'avez pas fait un choix",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        """
        je pouvais utiliser un redirect classique pour aller sur results_url mais utiliser la méthode
        HttpRespondeRedirect me permet d'éviter les d'enregistrer les données 2x et d'empecher l'user
        de faire un retour et voter encore ( Djo on sait jamais).
        """
        return HttpResponseRedirect(reverse('Vote:results_url', args=(question_id,)))


@login_required(login_url='/comptes/login/')
def resultsData(request, obj):
    votedata = []
    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()
    for i in votes:
        votedata.append({i.choice_text: i.votes})
    print(votedata)
    return JsonResponse(votedata, safe=False)
