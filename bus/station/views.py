from django.shortcuts import render
from .models import Routes
from django.views.generic import ListView
# Create your views here.

class RouteList(ListView):
    model = Routes
    template_name = 'route.html'
    context_object_name = 'routes'
    queryset = Routes.objects.all()