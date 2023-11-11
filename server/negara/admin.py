from django.contrib import admin
from .models import negara, kategori


class negaraAdmin(admin.ModelAdmin):
    list_display = ('asia', 'eropa',)

admin.site.register(negara, negaraAdmin)
admin.site.register(kategori)

# Register your models here.
