from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import AccountForm
from .models import Account


def home(request):
    accounts = request.user
    context = {
        "accounts": accounts,
    }
    return render(request, "index.html", context)
    # return HttpResponse(f"<h1>Welcome, {user}</h1>")


def createNewAccount(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = AccountForm()
    context = {
        'form': form,
    }
    return render(request, 'checkbook/CreateNewAccount.html', context)


def addTransaction(request):
    context = {}
    return render(request, 'AddTransaction.html', context)
