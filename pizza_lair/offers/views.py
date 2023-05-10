from django.shortcuts import render, get_object_or_404
from offers.models import Offer
from menu.models import Pizza, Drink, Side
# Create your views here.
def index(request):
    return render(request, 'offers/offers.html', {
        'offers': Offer.objects.all()
    })


def get_offer_by_id(request, id):
    if request.method == 'POST':
        print(request.POST)
        request.POST['pizzas']
    offer = get_object_or_404(Offer, pk=id)
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
    return render(request, 'offers/offer_details.html', {
        'offer': offer,
        'pizza_amount': pizza_amount,
        'sides_amount': sides_amount,
        'drinks_amount': drinks_amount,
        "pizzas": Pizza.objects.all(),
        "drinks": Drink.objects.all(),
        "sides": Side.objects.all()

    })



