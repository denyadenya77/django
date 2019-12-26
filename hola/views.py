from django.shortcuts import render
from django.http import HttpResponse
from .models import BotTable

# Create your views here.


def home_page_view(request):
    x = request.GET
    code = x['code']

    new_code = BotTable(code=code)
    new_code.save()

    return HttpResponse('Hola means hello in Spanish')