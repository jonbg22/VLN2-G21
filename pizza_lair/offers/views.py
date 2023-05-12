from django.shortcuts import render, get_object_or_404
from offers.models import Offer, get_todays_pizza
from menu.models import Pizza, Drink, Side
from json import loads, dumps
# Create your views here.
def index(request):
    return render(request, 'offers/offers.html', {
        'offers': Offer.objects.all(),
        'url': f'/offers'
    })


def get_offer_by_id(request, id):
    if request.method == 'POST':
        print(request.POST)
        cart_list = []
        if request.session.get('cart'):
            cart_list = loads(request.session.get('cart'))

        item_id = 1
        if len(cart_list) > 0:
            item_id = max(cart_list, key=lambda x: x["id"])["id"] + 1

        item = {"id": item_id, "offer_id": id, "type": "Offer"}
        if request.POST.get("pizzas"):
            item["pizzas"] = request.POST.getlist("pizzas")
        if request.POST.get("sides"):
            item["sides"] = request.POST.getlist("sides")
        if request.POST.get("drinks"):
            item["drinks"] = request.POST.getlist("drinks")
        cart_list.append(item)
        request.session["cart"] = dumps(cart_list)

    offer = get_object_or_404(Offer, pk=id)
    print("OFFER:",offer)
    pizza_amount = []
    for i in range(offer.amountPizza):
        i = i+1
        pizza_amount.append(i)
    sides_amount = []
    for i in range(offer.amountSides):
        i = i+1
        sides_amount.append(i)
    drinks_amount = []
    for i in range(offer.amountDrinks):
        i = i+1
        drinks_amount.append(i)

    if offer.name == "Pizza Of The Day":
        pizzas = [get_todays_pizza()]
    else:
        pizzas = Pizza.objects.all()
    return render(request, 'offers/offer_details.html', {
        'offer': offer,
        'pizza_amount': pizza_amount,
        'sides_amount': sides_amount,
        'drinks_amount': drinks_amount,
        "pizzas": pizzas,
        "drinks": Drink.objects.all(),
        "sides": Side.objects.all()

    })



