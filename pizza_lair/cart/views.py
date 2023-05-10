import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from json import loads
from menu.models import Product
from enum import Enum


def add_to_cart(request):
    print(request.method)
    if request.method == "DELETE":
        del request.session["cart"]
        print("DELETED", request.session.get('cart'))
        return HttpResponse("Done", status=200)

    if not request.method == "POST":
        return HttpResponseNotAllowed(['POST'])

    data = json.loads(request.body)
    if request.session.get("cart"):
        cart = json.loads(request.session.get("cart"))
        cart.append(data['id'])
        request.session["cart"] = json.dumps(cart)
    else:
        request.session["cart"] = json.dumps([data["id"]])

    return HttpResponse("Success")


def index(request):
    cart = []
    if request.session.get('cart'):
        id_list = []
        for prod_id in loads(request.session.get('cart')):
            if prod_id not in id_list:
                item = {
                    "type": "Product",
                    "count": 1,
                    "prod_id": prod_id,
                    "item": Product.objects.get(pk=prod_id)
                }
                cart.append(item)
                id_list.append(prod_id)
            else:
                for item in cart:
                    if item["prod_id"] == prod_id:
                        item["count"] += 1

    return render(request, 'cart/index.html', {
        'cart': cart
    })
