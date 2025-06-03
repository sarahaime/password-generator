import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest):
    return render(request, 'generator/home.html')


def about(request: HttpRequest):
    return render(request, 'generator/about.html')


def password(request: HttpRequest):
    length = int(request.GET.get('length', 12))
    characters=list('abcdefghyjklmnopqrstuvwxyz')
    generated_password = ''

    print(request.GET.get('uppercase'))

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special_characters'):
        characters.extend(list('!@#$%^&*()_+[-=}{]\/.,'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for i in range(0, length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})