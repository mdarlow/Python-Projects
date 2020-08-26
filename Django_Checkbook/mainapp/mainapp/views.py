from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    accounts = request.user
    context = {
        "accounts": accounts,
    }
    return render(request, "index.html", context)
    # return HttpResponse(f"<h1>Welcome, {user}</h1>")
