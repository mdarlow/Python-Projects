from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import AccountForm
from .models import Account


def createNewAccount(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print(form.errors)
        form = AccountForm()
    context = {
        'form': form,
    }
    return render(request, 'CreateNewAccount.html', context)
