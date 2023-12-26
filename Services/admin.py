from django.contrib import admin
from Services.models import Chinese, Italian, Indian_Street, North, South,Guj
from .models import Custom

class ChineseAdmin(admin.ModelAdmin):
    list_display=('product_id','chinese_icon','chinese_name','chinese_price', 'chinese_des')

admin.site.register(Chinese,ChineseAdmin)

class ItalianAdmin(admin.ModelAdmin):
    list_display=('product_id','italian_icon','italian_name','italian_price', 'italian_des')

admin.site.register(Italian,ItalianAdmin)

class StreetAdmin(admin.ModelAdmin):
    list_display=('product_id','street_icon','street_name','street_price', 'street_des')

admin.site.register(Indian_Street,StreetAdmin)

class NorthAdmin(admin.ModelAdmin):
    list_display=('product_id','north_icon','north_name','north_price', 'north_des')

admin.site.register(North,NorthAdmin)

class SouthAdmin(admin.ModelAdmin):
    list_display=('product_id','south_icon','south_name','south_price', 'south_des')

admin.site.register(South,SouthAdmin)

class GujAdmin(admin.ModelAdmin):
    list_display=('product_id','gujraj_icon','gujraj_name','gujraj_price', 'gujraj_des')

admin.site.register(Custom)

admin.site.register(Guj,GujAdmin)