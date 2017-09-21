from django.shortcuts import render
# from django.urls import reverse
# from django.core import serializers
# from .models import MajorReservoirs, RWPAs
from .config import layers


def index(request, letter=""):
    context = {'layers': layers, 'region': letter}
    return render(request, 'map/index.html', context)
