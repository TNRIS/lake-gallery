from django.shortcuts import render
# from django.urls import reverse
from django.core import serializers
# from .models import MajorReservoirs, RWPAs
from .config import layers
import json


def index(request, letter=""):
    if letter == "":
        layer = layers['rwpas']
    else:
        layer = layers['reservoirs']
    print(letter)
    # print(json.loads(json.dumps(layer)))
    context = {'layer': layer}

    return render(request, 'map/index.html', context)
