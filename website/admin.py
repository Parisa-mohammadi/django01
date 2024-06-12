from django.contrib import admin
from website.models import Contact, Newsletter


# Register your models here.
class ContAdmin(admin.ModelAdmin):
    name = 'name'
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'message', 'created_date', 'updated_date')


admin.site.register(Contact, ContAdmin)
admin.site.register(Newsletter)
