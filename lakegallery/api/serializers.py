from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from map.models import MajorReservoirs, RWPAs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ReservoirsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MajorReservoirs
        fields = ('res_lbl', 'region')


class RWPAsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RWPAs
        geo_field = 'geom'
        auto_bbox = True
        fields = ('reg_name', 'letter')
