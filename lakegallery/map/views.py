from django.shortcuts import render, redirect
from .config import layers

from django.shortcuts import render_to_response
# from django.template import RequestContext
from .models import MajorReservoirs, RWPAs, HistoricalAerialLinks, StoryContent


"""
utility functions
"""


def get_region_header_list():
    l = RWPAs.objects.values_list('reg_name', 'letter')
    labels = [{'name': r[0], 'letter': r[1]} for r in l]
    labels.sort(key=lambda x: x['name'])
    return labels


def get_lake_header_list():
    r = MajorReservoirs.objects.values_list('res_lbl', 'region')
    res = [{'name': n[0], 'region': n[1]} for n in r]
    res.sort(key=lambda x: x['name'])
    return res


"""
views/templates & redirects
"""


def index(request, letter=""):
    labels = get_region_header_list()
    res = get_lake_header_list()
    context = {'header_regions': labels, 'header_lakes': res,
               'layers': layers, 'region': letter}

    return render(request, 'map/index.html', context)


def redirect_region(request, letter):
    uppercase = letter.upper()
    return redirect('/' + uppercase)


def story(request, letter, lake):
    labels = get_region_header_list()
    res = get_lake_header_list()

    m = MajorReservoirs.objects.get(res_lbl=lake)
    n = HistoricalAerialLinks.objects.filter(lake=m)
    links = [obj.as_dict() for obj in n]
    links.sort(key=lambda x: x['year'])

    try:
        c = StoryContent.objects.get(lake=m)
    except:
        c = {'summary': 'summary pending...',
             'history': 'history pending...'}

    context = {'header_regions': labels, 'header_lakes': res,
               'layer': layers['reservoirs'], 'lake': lake, 'links': links,
               'story': c}

    return render(request, 'map/story.html', context)


"""
error code handling
"""


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
