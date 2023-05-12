from django.shortcuts import render
import datetime
from offers.models import get_todays_pizza
from menu.models import Pizza


def index(request):
    today = datetime.datetime.today()
    day_int = today.weekday()
    return render(request, 'index.html', {
        "weekday": today.strftime('%A'),
        'pizza': get_todays_pizza()
    })
