from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

user = [
    'ali','jakob','abtin'
]

def account(request,username):
    if username in user:
        return HttpResponse(f"my account is{username} ") 
    else:
        return HttpResponse("this user is not found")    