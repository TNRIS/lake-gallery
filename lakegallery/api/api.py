from rest_framework import routers
from .views import (ReservoirsViewSet, RWPAsReservoirsViewSet)
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

# main routes
reservoirs_router = router.register(r'reservoirs', ReservoirsViewSet,
                                    'api_reservoirs')
