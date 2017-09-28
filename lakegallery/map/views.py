from django.shortcuts import render, redirect
from .config import layers

from django.shortcuts import render_to_response
# from django.template import RequestContext
from .models import MajorReservoirs, RWPAs, HistoricalAerialLinks


def index(request, letter=""):
    l = RWPAs.objects.values_list('reg_name', 'letter')
    labels = [{'name': r[0], 'letter': r[1]} for r in l]
    labels.sort(key=lambda x: x['name'])
    # print(labels)
    r = MajorReservoirs.objects.values_list('res_lbl', 'region')
    res = [{'name': n[0], 'region': n[1]} for n in r]
    res.sort(key=lambda x: x['name'])
    # print(res)
    context = {'header_regions': labels, 'header_lakes': res,
               'layers': layers, 'region': letter}
    return render(request, 'map/index.html', context)


def redirect_region(request, letter):
    uppercase = letter.upper()
    return redirect('/' + uppercase)


def story(request, letter, lake):
    r = MajorReservoirs.objects.get(res_lbl=lake)
    l = HistoricalAerialLinks.objects.filter(lake=r)
    links = [obj.as_dict() for obj in l]
    links.sort(key=lambda x: x['year'])
    context = {'layer': layers['reservoirs'], 'lake': lake, 'links': links}
    return render(request, 'map/story.html', context)


def bad_request(request):
    context = {'code': 400, 'text': 'Bad Request'}
    response = render_to_response('map/error.html', context)
    response.status_code = 400
    return response


def permission_denied(request):
    context = {'code': 403, 'text': 'Permission Denied'}
    response = render_to_response('map/error.html', context)
    response.status_code = 403
    return response


def page_not_found(request):
    context = {'code': 404, 'text': 'Page Not Found'}
    response = render_to_response('map/error.html', context)
    response.status_code = 404
    return response


def server_error(request):
    context = {'code': 500, 'text': 'Server Error'}
    response = render_to_response('map/error.html', context)
    response.status_code = 500
    return response
