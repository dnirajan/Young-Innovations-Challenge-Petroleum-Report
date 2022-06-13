from django.contrib import admin
from deserialize.models import Country, PetroleumProduct, Detail, Year

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(PetroleumProduct)
class PetroleumProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['date']        
    
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['year','petroleum_product', 'country','sale']
