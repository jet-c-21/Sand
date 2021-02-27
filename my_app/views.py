from django.shortcuts import render
from django.http import HttpResponse
from .crawler import LACraigList
from . import models


# Create your views here.
def home(request) -> HttpResponse:
    return render(request, 'base.html')


def new_search(request) -> HttpResponse:
    search_str = request.POST.get('search')

    if not search_str:
        return home(request)

    # record to db
    models.Search.objects.create(search=search_str)

    min_price = request.POST.get('min-price')
    max_price = request.POST.get('max-price')
    LACraigList.search(search_str, min_price, max_price)

    context_for_front_end = {
        'search': search_str
    }
    return render(request, 'my_app/new_search.html', context_for_front_end)
