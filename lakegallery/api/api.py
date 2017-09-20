from rest_framework import routers
from .views import (UserViewSet, GroupViewSet,
                    ReservoirsViewSet, RWPAsViewSet)
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()
users_router = router.register(r'users', UserViewSet)
groups_route = router.register(r'groups', GroupViewSet)
reservoirs_router = router.register(r'reservoirs', ReservoirsViewSet)
rwpas_router = router.register(r'rwpas', RWPAsViewSet)

# reservoirs nested routes
reservoirs_router.register(
    'region', ReservoirsViewSet,
    base_name='reservoirs-region',
    parents_query_lookups=['region'])

reservoirs_router.register(
    'name', ReservoirsViewSet,
    base_name='reservoirs-name',
    parents_query_lookups=['res_lbl'])

# rwpas nested routes
rwpas_router.register(
    'region', RWPAsViewSet,
    base_name='rwpas-region',
    parents_query_lookups=['letter'])
