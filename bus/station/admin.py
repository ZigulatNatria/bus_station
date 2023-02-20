from django.contrib import admin
from .models import Routes, Bus, Vacancies, Gallery, Photo, News, RoutesCity, Contacts, \
    PhotoCarusel, History
# Register your models here.
admin.site.register(Routes)
admin.site.register(Bus)
admin.site.register(Vacancies)
admin.site.register(Gallery)
admin.site.register(Photo)
admin.site.register(News)
admin.site.register(RoutesCity)
admin.site.register(Contacts)
admin.site.register(PhotoCarusel)
admin.site.register(History)