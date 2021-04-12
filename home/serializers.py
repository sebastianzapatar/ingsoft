from rest_framework import serializers
from home.models import Cancion
class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cancion
        fields=('id','nombre','autor')