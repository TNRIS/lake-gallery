from django_filters import rest_framework as filters

from map.models import MajorReservoirs


class URLFilter(filters.FilterSet):
    url = filters.CharFilter(method='filter_url_string')

    class Meta:
        model = MajorReservoirs
        fields = ('res_lbl', )

    # querying based on URL doesn't really make sense - see comments
    # in view.
    # filters just based on if the lake name is in the URL. Not the
    # best way to do this but not many other options.
    def filter_url_string(self, queryset, name, value):
        for i in queryset:
            nm = i.res_lbl
            if nm in str(value):
                return queryset.filter(res_lbl=nm)
