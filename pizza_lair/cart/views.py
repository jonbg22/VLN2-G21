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
    print("CART =",cart_list)
    data = json.loads(request.body)
    flag = False
    for item in cart_list:
        if item["prod_id"] == data["id"]:
            item["count"] += 1
            flag = True
    if not flag:
        item_id = 1
        if len(cart_list) > 0:
            item_id = max(cart_list, key=lambda x: x["id"])["id"] + 1
        item = {"id": item_id, "prod_id": data["id"], "count": 1}
        cart_list.append(item)
    request.session["cart"] = dumps(cart_list)
    return HttpResponse("Success")


def clear_cart(request):
    if request.method == "DELETE":
        del request.session["cart"]
        print("DELETED", request.session.get('cart'))
        return HttpResponse("Done", status=200)


def delete_item(request, item_id):
    if request.method == "DELETE":
        if request.session.get('cart'):
            cart_list: list = loads(request.session.get('cart'))
            print("List before", cart_list)
            print(request.GET.get('all'), type(request.GET.get('all')))
            if request.GET.get('all') == 'true':
                cart_list = [item for item in cart_list if int(item["id"]) != item_id]
            else:
                for ind,item in enumerate(cart_list):
                    if item["id"] == item_id:
                        item["count"] -= 1
                        break

            request.session["cart"] = dumps(cart_list)
            print("List after", cart_list)

        return HttpResponse("Ok")


def index(request):
    # del request.session['cart']
    cart = []
    if request.session.get('cart'):
        for cart_item in loads(request.session.get('cart')):
            print("ITEM ID:", cart_item["id"])
            item = {
                "id": cart_item["id"],
                "type": "Product",
                "count": cart_item["count"],
                "prod_id": cart_item["prod_id"],
                "item": Product.objects.get(pk=cart_item["prod_id"])
            }
            cart.append(item)

    return render(request, 'cart/index.html', {
        'cart': cart
    })

def checkout(request):
    pass
