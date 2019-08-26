from django.contrib import admin
from.models import Equity
# Register your models here.


@admin.register(Equity)
class EquityModelAdmin(admin.ModelAdmin):

    list_display = ['title', 'ticker', 'shares',]
    #readonly_fields = ('current_value','net_value',)



