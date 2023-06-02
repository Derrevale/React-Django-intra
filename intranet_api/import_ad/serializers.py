from rest_framework import serializers

from import_ad.models import SilvaUser


class SilvaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilvaUser
        fields = ('id', 'last_name', 'first_name', 'email', 'site')
