from rest_framework import generics
from .models import Consultorias
from .serializers import ConsultoriasSerializer


class ConsultoriasList(generics.ListCreateAPIView):
    queryset = Consultorias.consultoriasobjects.all()
    serializer_class = ConsultoriasSerializer

class ConsultoriasDetail(generics.RetrieveDestroyAPIView):
    queryset = Consultorias.objects.all()
    serializer_class = ConsultoriasSerializer