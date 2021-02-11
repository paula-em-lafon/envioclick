from django.contrib import admin
from .models import Waiter, Service, Table

class WaiterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Waiter, WaiterAdmin)

class TableAdmin(admin.ModelAdmin):
    pass
admin.site.register(Table, TableAdmin)

class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service, ServiceAdmin)