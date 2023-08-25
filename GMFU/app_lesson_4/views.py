from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<body><a href = 'http://127.0.0.1/lesson_4'>Домашка по 4 занятию</a></body>")
# Create your views here.
