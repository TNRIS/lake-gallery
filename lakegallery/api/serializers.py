from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.reverse import reverse

from map.models import MajorReservoirs, RWPAs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ReservoirsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MajorReservoirs
        geo_field = 'geom'
        auto_bbox = True
        fields = ('res_lbl', 'region')


class RWPAsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RWPAs
        geo_field = 'geom'
        auto_bbox = True
        fields = ('reg_name', 'letter')


class ReservoirURLSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField('get_lake_url')

    def get_lake_url(self, obj):
        lake_nm = obj.res_lbl
        lake_url = reverse('api_reservoirs-detail', args=[lake_nm],
                           request=self.context.get('request'))
        return lake_url

    class Meta:
        model = MajorReservoirs
        fields = ('res_lbl', 'url')
