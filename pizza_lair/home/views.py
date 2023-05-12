from django.shortcuts import render
import datetime

def index(request):
    return render(request, 'index.html', {
        "weekday": datetime.datetime.today().strftime('%A')
    })
