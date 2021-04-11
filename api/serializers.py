from rest_framework import serializers
from .models import Consultorias

class ConsultoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorias
        fields = ('id', 'empresa', 'cnpj', 'fantasia', 'endereco', 'iniciodecontrato', 'vigenciadecontrato', 'modalidade', 'area', 'normas')