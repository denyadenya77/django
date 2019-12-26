from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_second_view(request):
    return HttpResponse('Privet means hello in russian')