""" Modulul care se ocupa cu transformarea modelelor din baza de date in 
    format json. """
from rest_framework import serializers
from .models import Cuvant, Definitie


class DefinitieSerializer(serializers.HyperlinkedModelSerializer):
    """ Clasa care specifica criteriul de formare a raspunsului JSON pentru
        modelul Definitie. """
    class Meta:
        model = Definitie
        fields = ["definitie_text"]


class CuvantSerializer(serializers.HyperlinkedModelSerializer):
    """ Clasa care specifica criteriul de formare a raspunsului JSON pentru
        modelul Cuvant. """
    definitii = DefinitieSerializer(source="definitie_set", many=True)
    
    class Meta:
        model = Cuvant
        fields = ["cuvant_text", "definitii"]
