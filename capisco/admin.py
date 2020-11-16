from django.contrib import admin
from .models import Tulkkaa


class TulkkaaAdmin(admin.ModelAdmin):
    list_display = ['kielinimi', 'fkieli', 'tkieli']
    list_editable = ['fkieli', 'tkieli']


admin.site.register(Tulkkaa, TulkkaaAdmin)