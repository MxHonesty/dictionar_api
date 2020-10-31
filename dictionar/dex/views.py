from rest_framework import viewsets
from rest_framework import permissions
from .models import Cuvant, Definitie
from rest_framework.response import Response
from .serializers import CuvantSerializer


class CuvantViewSet(viewsets.ModelViewSet):
    """ API ENDPOINT care permite vizualizarea sau editarea cuvintelor. """
    serializer_class = CuvantSerializer
    queryset = Cuvant.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        queryset = Cuvant.objects.all()
        serializer = CuvantSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, cuvant_text=None, pk=None):
        try:
            cuvant = Cuvant.objects.get(cuvant_text=cuvant_text)
        except Cuvant.DoesNotExist: 
            cuvant = Cuvant
        serializer = CuvantSerializer(cuvant)
        return Response(serializer.data)
