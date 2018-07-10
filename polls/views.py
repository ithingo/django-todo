# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, I am here with the simpliest django view')
