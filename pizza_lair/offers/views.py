from django.shortcuts import render, get_object_or_404
from offers.models import Offer
# Create your views here.
def index(request):
    return render(request, 'offers/offers.html', {
        'offers': Offer.objects.all()
    })

def get_offer_by_id(request, id):
    return render(request, 'offers/offer_details.html', {
        'offer': get_object_or_404(Offer, pk=id)
    })

