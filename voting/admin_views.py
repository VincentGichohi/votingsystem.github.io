from django.shortcuts import render
from account.views import account_login


def index(request):
    if not request.user.is_authenticated:
        return account_login(request)
    context = {}
    # return render(request, 'voting/login.html', context)
