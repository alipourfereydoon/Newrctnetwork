from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def account(request,username):
    return render(request,'account_app/account.html')  