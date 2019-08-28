from django.shortcuts import render, get_object_or_404
from .serializers import EquitySerializer
from .models import Equity
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response



class EquityView(viewsets.ModelViewSet):

    queryset = Equity.objects.all()
    serializer_class = EquitySerializer
    total = 0
    
    def list(self, request, *args, **kwargs):

        equities = self.queryset
        serializer = EquitySerializer(equities, many=True)
        data = serializer.data
        for i in range(len(data)):
            f = data[i]['current_equity_market']
            self.total = self.total + float(f)
        return Response({'Total Value of Portfolio ':self.total, 'Equities': serializer.data})