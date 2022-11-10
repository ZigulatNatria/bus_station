from django.shortcuts import render, redirect
from .models import Routes, Bus, Vacancies, Gallery, Photo, News #BusRoutes
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
# Create your views here.

class RouteList(ListView):
    model = Routes
    template_name = 'route1.html'
    context_object_name = 'routes'
    queryset = Routes.objects.all()


# class BusList(ListView):
#     model = Bus
#     template_name = 'by_routes.html'
#     context_object_name = 'buses'
#     queryset = Bus.objects.all()


class VacanciesList(ListView):
    model = Vacancies
    template_name = 'vacancies.html'
    context_object_name = 'vacancies'
    queryset = Vacancies.objects.all()


class VacanciesDetail(DetailView):
    template_name = 'vacancies_detail.html'
    context_object_name = 'vacanci'
    queryset = Vacancies.objects.all()

class NewsList(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    queryset = News.objects.all()


class NewsDetail(DetailView):
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'
    queryset = News.objects.all()


class GalleryListlView(ListView):
    model = Gallery
    context_object_name = 'galleries'
    template_name = 'gallery.html'
    queryset = Gallery.objects.all()


def by_galleries(request, photoGallery_id):
    image = Photo.objects.filter(photoGallery=photoGallery_id)
    galleryPhoto = Gallery.objects.all()
    current_gallery = Gallery.objects.get(pk=photoGallery_id)
    context = {'image': image, 'galleryPhoto': galleryPhoto, 'current_gallery': current_gallery}
    return render(request, 'by_galleries.html', context)


def by_routes(request, routes_id):
    bus = Bus.objects.filter(routes=routes_id)
    busRoutes = Routes.objects.all()
    current_routes = Routes.objects.get(pk=routes_id)
    context = {'bus': bus, 'busRoute': busRoutes, 'current_routes': current_routes}
    return render (request, 'by_routes1.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Отклик на вакансию"
            body = {
                'name': form.cleaned_data['name'],
                'telephone': form.cleaned_data['telephone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values()) #при переписывании на цифры в формах вылетает ошибка типов
            try:
                send_mail(subject, message,
                          'vachrameev.oleg@yandex.ru',
                          ['vachrameev.oleg@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("/bus/vacancies")
        else:
            messages.error(request, 'НЕПРАВИЛЬНО ВВЕДЁН КОД С КАРТИНКИ') #сообщение если капча не верна

    form = ContactForm()
    return render(request, "vacancies_mail.html", {'form': form})

# def index(request):
#     return render(request, 'index.html')
#
# def qq(request):
#     return render(request, 'qq.html')