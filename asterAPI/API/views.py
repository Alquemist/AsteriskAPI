from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import json

from .models import Cdr
from .serializers import CdrSerializer


class CdrViewSet(viewsets.ModelViewSet):
    queryset = Cdr.objects.all()
    @action(methods=['get'], detail=False)
    def lastCall(self, request):
        serialized = CdrSerializer(Cdr.objects.last())
        print(type(serialized))
        print(serialized.data)
        return Response(serialized.data)

    @action(methods=['get'], detail=False)
    def lastNCalls(self, request):
        n = request.GET.get('n', default=None)
        print('n=',n)
        try:
            serializedData = CdrSerializer(Cdr.objects.all().order_by('calldate')[:int(n)], many=True).data
        except Exception as err:
            print(err)
        return Response(serializedData)

