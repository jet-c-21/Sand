from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request) -> HttpResponse:
    return render(request, 'base.html')


def new_search(request) -> HttpResponse:
    search = request.POST.get('search')
    context_for_front_end = {
        'search': search
    }
    return render(request, 'my_app/new_search.html', context_for_front_end)
