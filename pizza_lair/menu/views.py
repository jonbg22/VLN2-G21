from django.shortcuts import render, get_object_or_404
from menu.models import Pizza

def index(request):
    return render(request, 'menu/index.html', {
        'pizzas': Pizza.objects.select_related("prod")
    })

def get_pizza_by_id(request,id):
    return render(request, 'menu/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


def sides(request):
    pass


def drinks(request):
    pass