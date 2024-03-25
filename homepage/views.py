from django.shortcuts import render

# Create your views here.#

from django.http import HttpResponse

from django.template import loader


def index(request):
    template_name = 'homepage/index.html'
    title = 'Главная страница АСМЕ'
    promo_product = 'Iron carrot'
    context = {
        'title' : title,
        'promo_product' : promo_product
    }
    return render(request, template_name, context)