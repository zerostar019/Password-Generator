from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html', {'password': 'qweqweqwe'})

def password(request):
    charachters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        charachters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        charachters.extend(list('1234567890'))


    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charachters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    name = "Хатыпов Разиль Рафисович"
    post = "Генеральный директор компании Libra:"

    return render(request, 'generator/about.html', {'info': post,
                                                    'name': name})