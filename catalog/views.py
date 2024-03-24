from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def product_list(request):
    return HttpResponse('Список всего на свете')


def product_detail(request):
    return HttpResponse('Это определённо вещь')