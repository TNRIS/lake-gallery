from django.shortcuts import render
# from django.urls import reverse
# from django.core import serializers
# from .models import MajorReservoirs, RWPAs


def index(request, letter="", lake=""):
    # data = MajorReservoirs.objects.filter(region='B')
    # print(data)
    # json = serializers.serialize('json', data)
    # print(json)

    # print(reverse('map:rwpas'))

    if letter == "":
        layer = 'rwpas'
    else:
        layer = 'reservoirs'

    context = {'layer': layer}

    return render(request, 'map/index.html', context)
