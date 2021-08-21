from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Club Learn! I am on the inter-webs.")

# Create your views here.
