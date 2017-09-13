from django.contrib.auth.models import User, Group
from rest_framework import serializers

from map.models import MajorReservoirs, RWPAs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ReservoirsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MajorReservoirs
        fields = ('res_lbl', 'region')


class RWPAsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RWPAs
        fields = ('reg_name', 'letter')
