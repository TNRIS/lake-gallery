from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import (ReservoirsSerializer,
                          ReservoirURLSerializer)
from .filters import URLFilter

from rest_framework_extensions.mixins import NestedViewSetMixin

from map.models import MajorReservoirs


class ReservoirsViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Major Reservoirs to be listed or detailed
    """
    serializer_class = ReservoirsSerializer
    lookup_field = 'res_lbl'
    queryset = MajorReservoirs.objects.all().order_by('res_lbl')
    filter_fields = ('res_lbl', 'region')
