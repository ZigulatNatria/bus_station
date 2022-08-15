from django.urls import path
from .views import RouteList, by_routes

urlpatterns =[
    path('route', RouteList.as_view(), name='route'),
    path('route/<int:routes_id>/', by_routes, name='by_routes'),
]