# coding: utf8
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {'boldmessage': "I am bold font from the context"}
    
    return render(request, 'index.html', context)