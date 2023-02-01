from django.http import HttpResponse
from django.shortcuts import render
from cgitb import html
from urllib import request

def data(request):
    return HttpResponse("welcome to the first page")
