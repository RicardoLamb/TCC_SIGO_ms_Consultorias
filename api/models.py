# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class Consultorias(models.Model):
#     class ConsultoriasObjects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset().filter(modalidade='vigente')

#     options = ('assessoria', 'Assessoria'), ('consultoria', 'Consultoria'), ('assessoria e consultoria', 'Assessoria e Consultoria')

#     empresa = models.CharField(max_length=80)
#     cnpj = models.CharField(max_length=14)
#     fantasia = models.CharField(max_length=50)
#     endereco = models.CharField(max_length=50)
#     iniciodecontrato = models.CharField(max_length=20)
#     vigenciadecontrato = models.CharField(max_length=20)
#     modalidade = models.CharField(max_length=25, choices=options, default='assessoria')
#     area = models.TextField(null=True)
#     normas = models.TextField(null=True)
#     objects = models.Manager()
#     consultoriasobjects = ConsultoriasObjects()

# class Meta:
#     ordering = ('-assessoria',)

# def __str__(self):
#     return self.empresa

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Consultorias(models.Model):
    class ConsultoriasObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(modalidade='assessoria')
    
    options = ('assessoria', 'Assessoria'), ('consultoria', 'Consultoria'), ('assessoria e consultoria', 'Assessoria e Consultoria'),

    empresa = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=14)
    fantasia = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    iniciodecontrato = models.CharField(max_length=20)
    vigenciadecontrato = models.CharField(max_length=20)
    modalidade = models.CharField(max_length=25, choices=options, default='assessoria')
    area = models.TextField(null=True)
    normas = models.TextField(null=True)
    objects = models.Manager()
    consultoriasobjects = ConsultoriasObjects()

class Meta:
    ordering = ('-assessoria',)

def __str__(self):
    return self.empresa