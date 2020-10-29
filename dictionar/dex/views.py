from rest_framework import viewsets
from rest_framework import permissions
from .models import Cuvant, Definitie
from .serializers import CuvantSerializer, DefinitieSerializer


class CuvantViewSet(viewsets.ModelViewSet):
    """ API ENDPOINT care permite vizualizarea sau editarea cuvintelor. """
    queryset = Cuvant.objects.all()
    serializer_class = CuvantSerializer
    permission_classes = [permissions.IsAuthenticated]


class DefinitieViewSet(viewsets.ModelViewSet):
    """ API ENDPOINT care permite vizualizarea sau editarea definitiilor. """
    queryset = Cuvant.objects.all()
    serializer_class = DefinitieSerializer
    permission_classes = [permissions.IsAuthenticated]
