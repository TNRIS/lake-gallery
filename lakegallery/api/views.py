from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (UserSerializer, GroupSerializer,
                          RWPAsSerializer, ReservoirsSerializer)

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


class ReservoirsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MajorReservoirs to be viewed or edited.
    """
    queryset = MajorReservoirs.objects.all()
    serializer_class = ReservoirsSerializer


class RWPAsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows RWPAs to be viewed or edited.
    """
    queryset = RWPAs.objects.all()
    serializer_class = RWPAsSerializer
