from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    '''домашная страница'''
    return render(request, 'home.html')
