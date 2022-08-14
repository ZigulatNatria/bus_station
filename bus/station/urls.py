from django.urls import path
from .views import RouteList

urlpatterns =[
    path('route', RouteList.as_view(), name='route'),
]