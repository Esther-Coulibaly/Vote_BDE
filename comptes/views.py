from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse


def indexView(request):
    return render(request, 'index.html')


def apropos(request):
    return render(request, 'apropos.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Vote:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/Register now.html', {'form': form})


def listView(request):
    list_user = []
    name_users = User.objects.all()
    for i in name_users:
        list_user.append({i.username: i})
    print(list_user)
    return JsonResponse(list_user, safe=False)


def presentation(request):
    return render(request, 'presentation.html')
