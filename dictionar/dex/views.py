from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import Cuvant, Definitie
from rest_framework.response import Response
from .serializers import CuvantSerializer, DefinitieSerializer
from rest_framework.decorators import action


class CuvantViewSet(viewsets.ModelViewSet):
    """ API ENDPOINT care permite vizualizarea sau editarea cuvintelor. """
    serializer_class = CuvantSerializer
    queryset = Cuvant.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        queryset = Cuvant.objects.all()
        serializer = CuvantSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Cuvant.objects.all()
        cuvant = get_object_or_404(queryset, pk=pk)
        serializer = CuvantSerializer(cuvant)
        return Response(serializer.data)
