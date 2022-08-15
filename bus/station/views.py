from django.shortcuts import render
from .models import Routes, Bus #BusRoutes
from django.views.generic import ListView
# Create your views here.

class RouteList(ListView):
    model = Routes
    template_name = 'index.html'
    context_object_name = 'routes'
    queryset = Routes.objects.all()


# class BusList(ListView):
#     model = Bus
#     template_name = 'by_routes.html'
#     context_object_name = 'buses'
#     queryset = Bus.objects.all()


def by_routes(request, routes_id):
    bus = Bus.objects.filter(routes=routes_id)
    busRoutes = Routes.objects.all()
    current_routes = Routes.objects.get(pk=routes_id)
    context = {'bus': bus, 'busRoute': busRoutes, 'current_routes': current_routes}
    return render (request, 'by_routes.html', context)