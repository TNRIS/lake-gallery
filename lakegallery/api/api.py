from rest_framework import routers
from .views import (ReservoirsViewSet, RWPAsViewSet,
                    RWPAsReservoirsViewSet)
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

# main routes
reservoirs_router = router.register(r'reservoirs', ReservoirsViewSet,
                                    'api_reservoirs')
rwpas_router = router.register(r'rwpas', RWPAsViewSet, 'api_rwpas')

# rwpas nested routes
rwpas_router.register(
    'reservoirs', RWPAsReservoirsViewSet,
    base_name='api_rwpas_reservoirs',
    parents_query_lookups=['region'])
