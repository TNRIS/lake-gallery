from django.shortcuts import render, redirect
from django.http import Http404
from .config import layers, overlays, overlay_order

from django.shortcuts import render_to_response
# from django.template import RequestContext
from .models import (MajorReservoirs, RWPAs, HistoricalAerialLinks,
                     StoryContent, LakeStatistics, SignificantEvents)

from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings


"""
utility functions
"""


def get_region_header_list():
    l = RWPAs.objects.values_list('reg_name', 'letter')
    labels = [{'name': r[0], 'letter': r[1]} for r in l]
    labels.sort(key=lambda x: x['name'])
    return labels


def get_lake_header_list():
    r = MajorReservoirs.objects.values_list('res_lbl', 'region', 'story')
    res = [{'name': n[0], 'region': n[1], 'class': n[2]} for n
           in r]
    res.sort(key=lambda x: x['name'])
    return res


"""
views/templates & redirects
"""


def index(request):
    labels = get_region_header_list()
    res = get_lake_header_list()
    context = {'header_regions': labels, 'header_lakes': res,
               'layers': layers, 'version': settings.VERSION}

    return render(request, 'map/index.html', context)


def region(request, letter):
    labels = get_region_header_list()
    res = get_lake_header_list()

    r = RWPAs.objects.get(letter=letter)
    ext = list(GEOSGeometry(r.geom).extent)

    context = {'header_regions': labels, 'header_lakes': res,
               'layers': layers, 'region': letter, 'extent': ext}

    return render(request, 'map/region.html', context)


def redirect_region(request, letter):
    uppercase = letter.upper()
    return redirect('/' + uppercase)


def redirect_story(request, letter, lake):
    uppercase = letter.upper()
    return redirect('/' + uppercase + '/' + lake)


def story(request, letter, lake):
    labels = get_region_header_list()
    res = get_lake_header_list()

    m = MajorReservoirs.objects.get(res_lbl=lake)
    if m.region != letter:
        raise Http404()

    ext = list(GEOSGeometry(m.geom).extent)

    n = HistoricalAerialLinks.objects.filter(lake=m)
    links = [obj.as_dict() for obj in n]
    links.append({'year': 2015, 'link': 'https://webservices.tnris.org/arcgis/services/TOP/TOP15_NC_CIR_50cm/ImageServer/WMSServer'})
    links.append({'year': 2016, 'link': 'https://webservices.tnris.org/arcgis/services/NAIP/NAIP16_NC_CIR_1m/ImageServer/WMSServer'})
    links.sort(key=lambda x: x['year'])

    try:
        c = StoryContent.objects.get(lake=m)
    except:
        c = {}

    try:
        s = LakeStatistics.objects.get(lake=m)
        s = s.string_numbers()
        s = s.set_displays()
    except:
        s = {}

    try:
        h = SignificantEvents.objects.filter(lake=m, event_type='High')
        high_list = [obj.as_dict() for obj in h]
        high_list.sort(key=lambda x: x['height'])
        high_list.reverse()
        for h in high_list:
            rank = high_list.index(h)
            rank += 1
            h['rank'] = rank
            del h['drought']
        if len(high_list) > 10:
            high_list = high_list[:10]
    except:
        high_list = []

    try:
        l = SignificantEvents.objects.filter(lake=m, event_type='Low')
        low_list = [obj.as_dict() for obj in l]
        low_list.sort(key=lambda x: x['height'])
        for l in low_list:
            rank = low_list.index(l)
            rank += 1
            l['rank'] = rank
        if len(low_list) > 10:
            low_list = low_list[:10]
    except:
        low_list = []

    context = {'header_regions': labels, 'header_lakes': res, 'extent': ext,
               'layer': layers['reservoirs'], 'lake': lake, 'links': links,
               'story': c, 'stats': s, 'high_events': high_list,
               'low_events': low_list, 'overlays': overlays,
               'overlay_order': overlay_order, 'overlay_query': m.id}

    if request.is_mobile is False:
        return render(request, 'map/story.html', context)
    else:
        return render(request, 'map/story_mobile.html', context)


"""
error code handling
"""


def bad_request(request):
    labels = get_region_header_list()
    res = get_lake_header_list()

    snark = "Maybe this story book is in a different language?"

    context = {'header_regions': labels, 'header_lakes': res,
               'code': 400, 'text': 'Bad Request',
               'snark': snark}
    response = render_to_response('map/error.html', context)
    response.status_code = 400
    return response


def permission_denied(request):
    labels = get_region_header_list()
    res = get_lake_header_list()

    snark = "Sorry, this story book is locked down."

    context = {'header_regions': labels, 'header_lakes': res,
               'code': 403, 'text': 'Permission Denied',
               'snark': snark}
    response = render_to_response('map/error.html', context)
    response.status_code = 403
    return response


def page_not_found(request):
    labels = get_region_header_list()
    res = get_lake_header_list()

    snark = ("Seems like you're looking for a page that's not in this story "
             "book.")

    context = {'header_regions': labels, 'header_lakes': res,
               'code': 404, 'text': 'Page Not Found',
               'snark': snark}
    response = render_to_response('map/error.html', context)
    response.status_code = 404
    return response


def server_error(request):
    labels = get_region_header_list()
    res = get_lake_header_list()

    snark = "Looks like the bookshelf fell out from under this story book."

    context = {'header_regions': labels, 'header_lakes': res,
               'code': 500, 'text': 'Server Error',
               'snark': snark}
    response = render_to_response('map/error.html', context)
    response.status_code = 500
    return response
