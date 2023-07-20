from django.contrib.auth.models import User, Group
from .models import Edificio, Departamento

from rest_framework import serializers


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = "__all__"


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"
