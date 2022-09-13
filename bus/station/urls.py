from django.urls import path
from .views import RouteList, VacanciesList, VacanciesDetail, by_routes, index, contact, qq, \
    GalleryListlView, by_galleries

urlpatterns =[
    path('', index, name='index'),
    path('route', RouteList.as_view(), name='route'),
    path('route/<int:routes_id>/', by_routes, name='by_routes'),
    path('vacancies', VacanciesList.as_view(), name='vacancies'),
    path('<int:pk>', VacanciesDetail.as_view(), name='vacancies_detail'),
    path('mail', contact, name='contact'),
    path('qq', qq, name='qq'),
    path('gallery', GalleryListlView.as_view(), name='gallery'),
    path('gallery/<int:photoGallery_id>/', by_galleries, name='by_galleries'),
]