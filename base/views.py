from asyncio import Task
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
# Create your views here.
def taskList (request):
    return HttpResponse('TO do list'),

    