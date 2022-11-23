from django.urls import path
from .views import RouteList, VacanciesList, VacanciesDetail, by_routes, contact,\
    GalleryListlView, NewsList, by_galleries, NewsDetail, search

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
]