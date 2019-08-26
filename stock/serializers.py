from rest_framework import serializers
from .models import Equity

from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries

class EquitySerializer(serializers.ModelSerializer, serializers.Serializer):

    
    fx_rate = serializers.SerializerMethodField('get_new_fx')
    def get_new_fx(self, obj):
        currency = ForeignExchange(key='WN9UYF2SGX9V3P0S')
        data = currency.get_currency_exchange_rate(from_currency='EUR', to_currency='USD')
        #latest = (data['2019-08-26 07:30:00'])
        #print(latest['2. high'])
        now = data[0]
        return now['5. Exchange Rate']
    
    current_equity_market = serializers.SerializerMethodField('get_current_equity_market')
    def get_current_equity_market(self, obj):

        equity = Equity.objects.all()
        print(Equity.objects.get(ticker='APC').ticker)
        stock = TimeSeries('WN9UYF2SGX9V3P0S')
        data, meta_data = stock.get_batch_stock_quotes(symbols=Equity.objects.get(ticker='APC').ticker)
        now = data[0]
        return now['2. price']
   
    current_value = serializers.SerializerMethodField('get_current_value')
    def get_current_value(self, obj):

        print(self.get_current_equity_market)

    class Meta:
        model = Equity
        fields = ['title', 'ticker', 'shares','fx_rate','current_equity_market', 'current_value']

