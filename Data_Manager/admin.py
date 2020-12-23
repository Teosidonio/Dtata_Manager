from django.contrib import admin
from Data_Manager.models import Environment
#from Data_Manager.models import EnvironmentBulkUpload

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('stage', 'platform', 'database', 'run_stack', 'web_server', 'ip_servername', 'hardware', 'product_app', 'provider', 'port', 'created_by', 'creation_date', 'brd')

# Register your models here.
admin.site.register(Environment, EnvironmentAdmin)