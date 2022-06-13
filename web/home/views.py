from random import random
from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

def home(request):
     return render(request, 'home.html')

def services(request):
     return render(request, 'services.html')

def password(request):
     characters = list('abcdefghijklmnopqrstvwxyz')

     GeneratedPassword = ''

     lenght = int(request.GET.get('lenght'))

     if(request.GET.get('uppercase')):
          characters.extend(list('ABCDEFGHIJKLMNOPQRSTVWXYZ'))

     if(request.GET.get('special')):
          characters.extend(list('_,./+-$%!@#*&^|]}{'))

     if(request.GET.get('numbers')):
          characters.extend(list('1234567890'))


     for x in range(lenght):
          GeneratedPassword += random.choice(characters)

     return render(request, 'password.html', {'password': GeneratedPassword})