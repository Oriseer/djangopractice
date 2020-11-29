from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello")

def product(request):
    return HttpResponse("product page")

def customer(request):
    return HttpResponse("customer page")
