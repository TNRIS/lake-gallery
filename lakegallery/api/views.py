from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (UserSerializer, GroupSerializer,
                          RWPAsSerializer, ReservoirsSerializer)

from rest_framework_extensions.mixins import NestedViewSetMixin

from map.models import MajorReservoirs, RWPAs


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ReservoirsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows MajorReservoirs to be listed or detailed
    """
    serializer_class = ReservoirsSerializer
    lookup_field = 'res_lbl'
    queryset = MajorReservoirs.objects.all().order_by('res_lbl')


class RWPAsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows RWPAs regions to be listed or detailed
    """
    serializer_class = RWPAsSerializer
    lookup_field = 'letter'
    queryset = RWPAs.objects.all().order_by('letter')


class RWPAsReservoirsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    API endpoint that returns the reservoirs for the specified region
    """
    serializer_class = ReservoirsSerializer
    queryset = MajorReservoirs.objects.all().order_by('res_lbl')
