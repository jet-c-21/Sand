from django.shortcuts import render
from django.http import HttpResponse
from .crawler import LACraigList
from . import models


# Create your views here.
def home(request) -> HttpResponse:
    return render(request, 'base.html')


def new_search(request) -> HttpResponse:
    search_str = request.POST.get('search')
    # record to db
    models.Search.objects.create(search=search_str)

    LACraigList.search(search_str)

    context_for_front_end = {
        'search': search_str
    }
    return render(request, 'my_app/new_search.html', context_for_front_end)
