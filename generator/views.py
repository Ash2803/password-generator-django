from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    the_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_=-][{}'))
    if request.GET.get('Numbers'):
        characters.extend(list('01234567890'))
    length = int(request.GET.get('length', 12))
    for x in range(length):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': the_password})
