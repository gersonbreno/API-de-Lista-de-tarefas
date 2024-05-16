from lista.models import Listas
from rest_framework import status
from datetime import date
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, generics
from lista.api.serializers import ListaSerializer
from rest_framework.decorators import action
class ListaViewSet(ModelViewSet):
    serializer_class = ListaSerializer
    queryset = Listas.objects.all()
    @action(detail=True, methods=('post', 'get'))
    def finalizar_tarefa(self, request, pk = None):
        lista = self.get_object()
        lista.finalizado = True
        lista.data_fim = date.today()
        lista.save()
        Serializer = self.get_serializer(lista)
        return Response(Serializer.data)