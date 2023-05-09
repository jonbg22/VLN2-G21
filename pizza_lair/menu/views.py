from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Pizza, Side, Drink, PizzaCategory, Product
from django.core import serializers
import json


def addToCart(request):
    print(request.method)
    if request.method == "GET":
        del request.session["cart"]
        return HttpResponse("Done", status=200)

    if not request.method == "POST":
        return HttpResponseNotAllowed(['POST'])

    data = json.loads(request.body)
    print("CART:", type(request.session.get("cart")))
    if request.session.get("cart"):
        cart = json.loads(request.session.get("cart"))
        cart.append(data['id'])
        request.session["cart"] = json.dumps(cart)
    else:
        request.session["cart"] = json.dumps([data["id"]])
    print(request.session.get('cart'))
    return HttpResponse("Success")


def pizzas(request):
    flag = False
    filtered_pizzas = []
    all_pizzas = Pizza.objects.all()
    if request.GET.get('search') not in [None, ""]:
        flag = True
        search = request.GET['search']
        all_pizzas = all_pizzas.filter(prod__name__icontains=search)
    if request.GET.get('filter') not in [None, ""]:
        flag = True
        category_filter = request.GET['filter']
        if category_filter != "Any":
            all_pizzas = all_pizzas.filter(category__name=category_filter)
    if request.GET.get('orderBy') not in [None, ""]:
        flag = True
        order_by = request.GET['orderBy']
        if order_by == "Price":
            if request.GET.get('orderDir') == "descending":
                all_pizzas = all_pizzas.order_by("-prod__price")
            else:
                all_pizzas = all_pizzas.order_by("prod__price")
        elif order_by == "Name":
            if request.GET.get('orderDir') == "descending":
                all_pizzas = all_pizzas.order_by("-prod__name")
            else:
                all_pizzas = all_pizzas.order_by("prod__name")

    if flag:
        for pizza in all_pizzas:
            selected_pizza = {'id': pizza.id, 'prod_id': pizza.prod_id, 'prod': serializers.serialize('json', [pizza.prod, ])}
            filtered_pizzas.append(selected_pizza)
        return JsonResponse({'data': filtered_pizzas})

    return render(request, 'menu/pizzas.html', {
        'pizzas': Pizza.objects.select_related("prod")
    })


def get_pizza_by_id(request, id):
    if "addToCart" in request.GET:
        request.session['cart'] = "PIZZA"
        print(request.session.get('cart'))

    return render(request, 'menu/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, prod=id)
    })


def sides(request):
    return render(request, 'menu/sides.html', {
        'sides': Side.objects.select_related("prod")
    })


def get_side_by_id(request, id):
    return render(request, 'menu/side_details.html', {
        'side': get_object_or_404(Side, prod=id)
    })


def drinks(request):
    return render(request, 'menu/drinks.html', {
        'drinks': Drink.objects.select_related("prod")
    })


def get_drink_by_id(request, id):
    return render(request, 'menu/drink_details.html', {
        'drink': get_object_or_404(Drink, prod=id)
    })
