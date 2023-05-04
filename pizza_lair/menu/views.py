from django.shortcuts import render, get_object_or_404
from menu.models import Pizza,Side,Drink

def index(request):
    return render(request, 'menu/pizzas.html', {
        'pizzas': Pizza.objects.select_related("prod")
    })

def get_pizza_by_id(request,id):
    return render(request, 'menu/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })


def sides(request):
    return render(request, 'menu/sides.html', {
        'sides': Side.objects.select_related("prod")
    })


def drinks(request):
    return render(request, 'menu/drinks.html', {
        'drinks': Drink.objects.select_related("prod")
    })