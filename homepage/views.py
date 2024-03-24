from django.shortcuts import render

# Create your views here.#

from django.http import HttpResponse

from django.template import loader


def index(request):
    template_name = 'homepage/index.html'
    return render(request, template_name)