from rest_framework import serializers
from .models import Equity
import requests, json 

from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries

class EquitySerializer(serializers.ModelSerializer, serializers.Serializer):

    currency = 0
    current_value = 0
    fx_rate = serializers.SerializerMethodField('get_new_fx')
    def get_new_fx(self, obj):
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=USD&apikey=WN9UYF2SGX9V3P0S'
        req = requests.get(url)
        result = req.json()
        self.currency = float(result["Realtime Currency Exchange Rate"] 
                ['5. Exchange Rate'])
        return (result["Realtime Currency Exchange Rate"] 
                ['5. Exchange Rate'])
    
    current_equity_market = serializers.SerializerMethodField('get_current_equity_market')
    def get_current_equity_market(self, obj):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={obj.ticker}&apikey=WN9UYF2SGX9V3P0S'
        req = requests.get(url)
        result = req.json()
        print(result)
        self.current_value = float(result["Global Quote"]['05. price'])
        return  (result["Global Quote"]['05. price'])
    
    def get_current_value(self, obj):
        stock = TimeSeries('WN9UYF2SGX9V3P0S')
        data, meta_data = stock.get_batch_stock_quotes(symbols=obj.ticker)
        current_market = data[0]
        currency = ForeignExchange(key='WN9UYF2SGX9V3P0S')
        data = currency.get_currency_exchange_rate(from_currency='EUR', to_currency='USD')
        currency_value = data[0]

        return_statmenet = float(currency_value['5. Exchange Rate'])*float(current_market['2. price'])*obj.shares
        return return_statmenet

    total_value_in_Equity = serializers.SerializerMethodField('get_total_equity_value')
    def get_total_equity_value(self, obj):
        return_statment = self.current_value*obj.shares
        return f'{return_statment} USD'
    
    total_value_in_portfolio_currency = serializers.SerializerMethodField('get_total_in_portfolio')
    def get_total_in_portfolio(self, obj):

        return_statment = self.currency*obj.shares*self.current_value
        return f'{return_statment} EUR'

    class Meta:
        model = Equity
        fields = ['title', 'ticker', 'shares','fx_rate','current_equity_market', 'total_value_in_Equity','total_value_in_portfolio_currency']
