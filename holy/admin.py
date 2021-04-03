from django.contrib import admin
from holy.models import NEW_ARRIVAL
from holy.models import CATE_GORY
from holy.models import Cart
from holy.models import Customer_detail
from holy.models import Order_place
# Register your models here.

admin.site.register(NEW_ARRIVAL)
admin.site.register(CATE_GORY)
admin.site.register(Cart)
admin.site.register(Customer_detail)
admin.site.register(Order_place)
