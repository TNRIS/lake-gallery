from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (UserSerializer, GroupSerializer,
                          RWPAsSerializer, ReservoirsSerializer,
                          ReservoirURLSerializer)

from rest_framework_extensions.mixins import NestedViewSetMixin

from map.models import MajorReservoirs, RWPAs


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ReservoirsViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows MajorReservoirs to be listed or detailed
    """
    serializer_class = ReservoirsSerializer
    lookup_field = 'res_lbl'
    queryset = MajorReservoirs.objects.all().order_by('res_lbl')


class RWPAsViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows RWPAs regions to be listed or detailed
    """
    serializer_class = RWPAsSerializer
    lookup_field = 'letter'
    queryset = RWPAs.objects.all().order_by('letter')


class RWPAsReservoirsViewSet(NestedViewSetMixin,
                             viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that returns the reservoirs for the specified region w/ URLs
    """
    serializer_class = ReservoirURLSerializer
    lookup_field = 'res_lbl'
    queryset = MajorReservoirs.objects.all().order_by('res_lbl')
