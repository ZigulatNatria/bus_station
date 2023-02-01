from django.urls import path
from .views import RouteList, VacanciesList, VacanciesDetail, by_routes, contact,\
    GalleryListlView, NewsList, by_galleries, NewsDetail, search, timetable_all, \
    CityBus, CityBusDetail, RoutesAddView, RoutesUpdateView, RoutesDeleteView, \
    NewsAddView, NewsUpdateView, NewsDeleteView

urlpatterns =[
    path('', NewsList.as_view() , name='news'),
    path('route', RouteList.as_view(), name='route'),
    path('route/<int:routes_id>/', by_routes, name='by_routes'),
    path('vacancies', VacanciesList.as_view(), name='vacancies'),
    path('<int:pk>', VacanciesDetail.as_view(), name='vacancies_detail'),
    path('mail', contact, name='contact'),
    path('gallery', GalleryListlView.as_view(), name='gallery'),
    path('gallery/<int:photoGallery_id>/', by_galleries, name='by_galleries'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('search/', search, name='search'),
    path('time/', timetable_all, name='time'),
    path('city_bus/', CityBus.as_view(), name='city_bus'),
    path('city_bus/<int:pk>/', CityBusDetail.as_view(), name='city_bus_detail'),
    path('city_bus_add/', RoutesAddView.as_view(), name='city_bus_add'),
    path('news_add/', NewsAddView.as_view(), name='news_add'),
    path('city_bus_update/<int:pk>/', RoutesUpdateView.as_view(), name='city_bus_update'),
    path('news_update/<int:pk>/', NewsUpdateView.as_view(), name='news_update'),
    path('city_bus_delete/<int:pk>/', RoutesDeleteView.as_view(), name='city_bus_delete'),
    path('news_delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
]