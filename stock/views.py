from django.shortcuts import render, get_object_or_404
from .serializers import EquitySerializer
from .models import Equity



from rest_framework import viewsets
from rest_framework.response import Response



class EquityView(viewsets.ModelViewSet):


    serializer_class = EquitySerializer
    queryset = Equity.objects.all()
    
    