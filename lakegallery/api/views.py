from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (RWPAsSerializer, ReservoirsSerializer,
                          ReservoirURLSerializer)
from .filters import URLFilter

from rest_framework_extensions.mixins import NestedViewSetMixin

from map.models import MajorReservoirs, RWPAs


class ReservoirsViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows MajorReservoirs to be listed or detailed
    """
    serializer_class = ReservoirsSerializer
    lookup_field = 'res_lbl'
    queryset = MajorReservoirs.objects.all().order_by('res_lbl')
    filter_fields = ('res_lbl', 'region')


class RWPAsViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows RWPAs regions to be listed or detailed
    """
    serializer_class = RWPAsSerializer
    lookup_field = 'letter'
    queryset = RWPAs.objects.all().order_by('letter')
    filter_fields = ('reg_name', 'letter')


class RWPAsReservoirsViewSet(NestedViewSetMixin,
                             viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that returns the reservoirs for the specified region w/ URLs
    """
    serializer_class = ReservoirURLSerializer
    lookup_field = 'res_lbl'
    queryset = MajorReservoirs.objects.all().order_by('res_lbl')

    # filter_fields = ('res_lbl', )
    filter_class = URLFilter
    # Uses custom filter_class opposed to out-of-the-box filter_fields to allow
    # question mark query/filtering against the serializer URL field. This is
    # not actually needed since a user who has the URL also has the lake name
    # and can (and probably should) query just using it but i set this up
    # regardless in the name of completeness.
