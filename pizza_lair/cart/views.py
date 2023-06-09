import json
from .forms.checkout_form import CheckoutForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from json import loads, dumps
from menu.models import Product, Pizza, Side, Drink
from offers.models import Offer
from users.models import Profile
from enum import Enum
from .forms.payment_form import PaymentForm
from django.contrib.auth.decorators import login_required

def add_to_cart(request):
    if not request.method == "POST":
        return HttpResponseNotAllowed(['POST'])

    cart_list = []
    if request.session.get('cart'):
        cart_list = loads(request.session.get('cart'))
    print("CART =", cart_list)
    data = json.loads(request.body)
    flag = False
    for item in cart_list:
        if item["type"] == "Product" and item["prod_id"] == data["id"]:
            item["count"] += 1
            flag = True
    if not flag:
        item_id = 1
        if len(cart_list) > 0:
            item_id = max(cart_list, key=lambda x: x["id"])["id"] + 1
        item = {"id": item_id, "prod_id": data["id"], "count": 1, "type": "Product"}
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
                    if item["id"] == item_id and item["count"] > 1:
                        item["count"] -= 1
                        break
                    elif item["count"] == 1:
                        cart_list = [item for item in cart_list if int(item["id"]) != item_id]

            request.session["cart"] = dumps(cart_list)
            print("List after", cart_list)

        return HttpResponse("Ok")


def index(request):
    # uncomment line to clear cart manually
    # del request.session['cart']
    cart = []
    cart_price = 0
    if request.session.get('cart'):
        for cart_item in loads(request.session.get('cart')):
            print("CUR ITEM", cart_item)
            if cart_item["type"] == "Product":
                prod_item = Product.objects.get(pk=cart_item["prod_id"])
                item = {
                    "id": cart_item["id"],
                    "type": "Product",
                    "count": cart_item["count"],
                    "prod_id": cart_item["prod_id"],
                    "item": prod_item,
                    "price": prod_item.price,
                    "total_price": prod_item.price * cart_item["count"]
                }
                cart_price += item["total_price"]
            else:
                cart_item: dict = cart_item
                offer = Offer.objects.get(pk=cart_item["offer_id"])
                item = {
                    "id": cart_item["id"],
                    "name": offer.name,
                    "type": "Offer",
                    "pizzas": [Pizza.objects.get(prod__id=prod_id) for prod_id in cart_item.get('pizzas', [])],
                    "sides": [Side.objects.select_related("prod").get(prod__id=prod_id) for prod_id in
                              cart_item.get('sides', [])],
                    "drinks": [Drink.objects.select_related("prod").get(prod__id=prod_id) for prod_id in
                               cart_item.get('drinks', [])],
                    "price": offer.price
                }
                cart_price += offer.price
            cart.append(item)

    return render(request, 'cart/index.html', {
        'cart': cart,
        'cart_price': cart_price
    })


@login_required
def checkout(request):
    checkout = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = CheckoutForm(instance=checkout, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('payment')
    return render(request, 'cart/checkout.html', {
        'form': CheckoutForm(instance=checkout)
    })

@login_required
def payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        request.session['card_name'] = request.POST['name_on_card']
        request.session['card_num'] = request.POST['card_number']
        request.session['card_date'] = request.POST['expiry_date']
        request.session['card_cvc'] = request.POST['cvc']
        if form.is_valid():
            return redirect('review')
    card_name = None
    card_num = None
    card_date = None
    card_cvc = None
    if 'card_num' in request.session:
        card_name = request.session['card_name']
        card_num = request.session['card_num']
        card_date = request.session['card_date']
        card_cvc = request.session['card_cvc']
    form = PaymentForm()
    form.fields["name_on_card"].initial = card_name
    form.fields["card_number"].initial = card_num
    form.fields["expiry_date"].initial = card_date
    form.fields["cvc"].initial = card_cvc
    return render(request, 'cart/payment.html', {'form': form})


@login_required
def review(request):
    card_info = {
        'card_name': request.session['card_name'],
        'card_num': request.session['card_num'][-4:],
        'card_date': request.session['card_date'],
        'card_cvc': request.session['card_cvc']
    }
    cart_list = []
    for item in loads(request.session.get('cart')):
        if item['type'] == "Product":
            cur_prod = Product.objects.get(pk=item["prod_id"])
            cart_list.append({
                'name': cur_prod.name,
                'count': item['count'],
                'price': cur_prod.price * item['count']
            })
        elif item['type'] == "Offer":
            offer = Offer.objects.get(pk=item['offer_id'])
            cart_list.append({
                'name': offer.name,
                'price': offer.price
            })

    return render(request, 'cart/review.html', {
        'card_info': card_info,
        'cart_list': cart_list,
        'profile': Profile.objects.filter(user=request.user).first()
    })

@login_required
def confirmation(request):
    del request.session['card_name'],
    del request.session['card_num'],
    del request.session['card_date'],
    del request.session['card_cvc']
    return render(request, 'cart/confirmation.html')
