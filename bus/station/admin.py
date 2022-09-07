from django.contrib import admin
from .models import Routes, Bus, Vacancies
# Register your models here.
admin.site.register(Routes)
admin.site.register(Bus)
admin.site.register(Vacancies)