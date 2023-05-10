import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from json import loads, dumps
from menu.models import Product
from enum import Enum


def add_to_cart(request):
    if not request.method == "POST":
        return HttpResponseNotAllowed(['POST'])
    cart_list = []
    if request.session.get('cart'):
        cart_list = loads(request.session.get('cart'))
    item_id = 1
    if len(cart_list) > 0:
        item_id = max(cart_list, key=lambda x: x["id"])["id"] + 1
    data = json.loads(request.body)
    item = {"id": item_id, "prod_id": data["id"]}
    if request.session.get("cart"):
        cart = json.loads(request.session.get("cart"))
        cart.append(item)
        request.session["cart"] = dumps(cart)
    else:

        request.session["cart"] = dumps([item])
    return HttpResponse("Success")


def clear_cart(request):
    if request.method == "DELETE":
        del request.session["cart"]
        print("DELETED", request.session.get('cart'))
        return HttpResponse("Done", status=200)


def delete_item(request, item_id):
    if request.method == "DELETE":
        if request.session.get('cart'):
            cart_list = loads(request.session.get('cart'))
            print("List before", cart_list)
            spliced_list = [item for item in cart_list if int(item["id"]) != item_id]
            print("List after", spliced_list)
            request.session["cart"] = dumps(spliced_list)
        return HttpResponse("Ok")


def index(request):
    # del request.session['cart']
    cart = []
    if request.session.get('cart'):
        id_list = []
        for cart_item in loads(request.session.get('cart')):
            if cart_item["prod_id"] not in id_list:
                print("ITEM ID:", cart_item["id"])
                item = {
                    "id": cart_item["id"],
                    "type": "Product",
                    "count": 1,
                    "prod_id": cart_item["prod_id"],
                    "item": Product.objects.get(pk=cart_item["prod_id"])
                }
                cart.append(item)
                id_list.append(cart_item["prod_id"])
            else:
                for item in cart:
                    if item["prod_id"] == prod_id:
                        item["count"] += 1

    return render(request, 'cart/index.html', {
        'cart': cart
    })
