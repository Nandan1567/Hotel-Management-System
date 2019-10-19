from django.shortcuts import render
from django.http import HttpResponse

def index(reqest):
    return HttpResponse('<h1> HOTEL MANAGEMENT SYSTEM </h1>')

# Create your views here.
