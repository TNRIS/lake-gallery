from django.shortcuts import render
from .models import MajorReservoirs, RWPAs


def index(request):
    # data = WorldBorder.objects.filter(name='United States')
    # print(data)
    # context = {'q': data[0]}
    # return render(request, 'world/index.html', context)
    return render(request, 'map/index.html')
