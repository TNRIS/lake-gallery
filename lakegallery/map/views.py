from django.shortcuts import render, redirect
from django.http import Http404

from django.shortcuts import render_to_response
# from django.template import RequestContext
from .models import (MajorReservoirs, HistoricalAerialLinks,
                     StoryContent, LakeStatistics, SignificantEvents)

from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings


"""
utility functions
"""


def get_lake_header_list():
    r = MajorReservoirs.objects.values_list('res_lbl', 'story')
    res = [{'name': n[0], 'class': n[1]} for n
           in r]
    res.sort(key=lambda x: x['name'])
    return res


"""
views/templates & redirects
"""


def index(request):
    res = get_lake_header_list()
    context = {'header_lakes': res,
               'version': settings.VERSION}

    return render(request, 'map/index.html', context)


def story(request, lake):
    res = get_lake_header_list()
    m = MajorReservoirs.objects.get(res_lbl=lake)

    ext = list(GEOSGeometry(m.geom).extent)

    n = HistoricalAerialLinks.objects.filter(lake=m)

    links = [obj.as_dict() for obj in n]
    links.append({'year': 2015, 'link': 'https://webservices.tnris.org/arcgis/services/TOP/TOP15_NC_CIR_50cm/ImageServer/WMSServer'})
    links.append({'year': 2016, 'link': 'https://webservices.tnris.org/arcgis/services/NAIP/NAIP16_NC_CIR_1m/ImageServer/WMSServer'})
    links.sort(key=lambda x: x['year'])

    datahub = []

    for obj in n:
        datahub.append({'year': obj.year, 'id': obj.datahub_collection_id})

    datahub.append({'year': 2015, 'id': 'b7e5b638-99f0-4676-9411-c88d06d49943'})
    datahub.append({'year': 2016, 'id': 'a40c2ff9-ccac-4c76-99a1-2382c09cf716'})
    datahub.sort(key=lambda x: x['year'])

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

    context = {'header_lakes': res, 'extent': ext,
               'lake': lake, 'links': links,
               'story': c, 'stats': s, 'high_events': high_list,
               'low_events': low_list,
               'data_hub_ids': datahub,
               'version': settings.VERSION}

    if request.is_mobile is False:
        return render(request, 'map/story.html', context)
    else:
        return render(request, 'map/story_mobile.html', context)


def about(request):
    res = get_lake_header_list()
    context = {'header_lakes': res,
               'version': settings.VERSION,
               'contact_submit_url': settings.CONTACT_SUBMIT_URL,
               'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY}

    return render(request, 'map/about.html', context)


"""
error code handling
"""


def bad_request(request):
    res = get_lake_header_list()

    snark = "Maybe this story book is in a different language?"

    context = {'header_lakes': res,
               'code': 400, 'text': 'Bad Request',
               'snark': snark}
    response = render_to_response('map/error.html', context)
    response.status_code = 400
    return response


def permission_denied(request):
    res = get_lake_header_list()

    snark = "Sorry, this story book is locked down."

    context = {'header_lakes': res,
               'code': 403, 'text': 'Permission Denied',
               'snark': snark}
    response = render_to_response('map/error.html', context)
    response.status_code = 403
    return response


def page_not_found(request):
    res = get_lake_header_list()

    snark = ("Seems like you're looking for a page that's not in this story "
             "book.")

    context = {'header_lakes': res,
               'code': 404, 'text': 'Page Not Found',
               'snark': snark}
    response = render_to_response('map/error.html', context)
    response.status_code = 404
    return response


def server_error(request):
    res = get_lake_header_list()

    snark = "Looks like the bookshelf fell out from under this story book."

    context = {'header_lakes': res,
               'code': 500, 'text': 'Server Error',
               'snark': snark}
    response = render_to_response('map/error.html', context)
    response.status_code = 500
    return response
