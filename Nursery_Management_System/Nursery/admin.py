from django.contrib import admin
from .models import Add_plant,order_plant1
# Register your models here.
class Add_plant_admin(admin.ModelAdmin) :
    list_display = ['plant_name','price','plant_type','imagefile']

class order_plant_Admin(admin.ModelAdmin) :
   list_display = ['Customer_Name','plant_name','qty','date']

admin.site.register(Add_plant,Add_plant_admin)
admin.site.register(order_plant1,order_plant_Admin)
