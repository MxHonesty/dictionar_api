from rest_framework import viewsets
from django.http import Http404
from rest_framework.response import Response
from rest_framework import permissions

from .models import Cuvant, Definitie
from .serializers import CuvantSerializer
import dex.dictionary as dict


class CuvantViewSet(viewsets.ModelViewSet):
    """ API ENDPOINT care permite vizualizarea sau editarea cuvintelor. """
    serializer_class = CuvantSerializer
    queryset = Cuvant.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        """ Functia apelata pentru obtinerea tuturor cuvintelor. """
        queryset = Cuvant.objects.all()
        serializer = CuvantSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, cuvant_text=None, pk=None):
        """ Functia apelata pentru obtinerea unui cuvant individual. """
        cuvant_text = cuvant_text.lower()
        try:
            cuvant = Cuvant.objects.get(cuvant_text=cuvant_text)
        except Cuvant.DoesNotExist: 
            definitie = dict.fetch_definition(cuvant_text)
            if definitie is None:
                raise Http404
            else:
                cuvant = Cuvant.objects.create(cuvant_text=cuvant_text,
                                               cautari=0)
                noua_definitie = Definitie.objects.create(definitie_text=definitie,
                                                          cuvant=cuvant)
                        
        serializer = CuvantSerializer(cuvant)
        return Response(serializer.data)
