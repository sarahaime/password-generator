import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest):
    return render(request, 'generator/home.html', {'password': 'fiuhsdfliguh'})


def password(request: HttpRequest):
    length = int(request.GET.get('length', 12))
    characters=list('abcdefghyjklmnopqrstuvwxyz')
    generated_password = ''

    for i in range(0, length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})