from django.urls import path
from .views import ConsultoriasList, ConsultoriasDetail

app_name = 'consultorias_api'

urlpatterns = [
    path('<int:pk>/', ConsultoriasDetail.as_view(), name='detailcreate'),
    path('', ConsultoriasList.as_view(), name='listcreate'),
]