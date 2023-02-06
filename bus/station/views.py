from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Routes, Bus, Vacancies, Gallery, Photo, News, RoutesCity #BusRoutes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, RoutesCityForm, NewsForm, VacanciesForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_aut'] = self.request.user.groups.exists()
        return context


class VacanciesDetail(DetailView):
    template_name = 'vacancies_detail.html'
    context_object_name = 'vacanci'
    queryset = Vacancies.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_aut'] = self.request.user.groups.exists()
        return context


class NewsList(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    queryset = News.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_aut'] = self.request.user.groups.exists()
        return context


class NewsDetail(DetailView):
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'
    queryset = News.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_aut'] = self.request.user.groups.exists()
        return context


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


def search(request):
    search_query = request.GET.get('search', '') # передаётся имя ввода (строка поиска)

# если значение search_query существует (в строку поиска введён текст) ищем в нужных полях введённый текст
    if search_query:
        news = News.objects.filter(news_header__icontains=search_query) #TODO доделать поиск
    else:
        news = News.objects.all()
    context = {'news': news}
    return render(request, 'search.html', context)

def timetable_all(request):
    return render(request, 'timetable.html')

class CityBus(ListView):
    model = RoutesCity
    template_name = 'city_bus.html'
    context_object_name = 'buses'
    queryset = RoutesCity.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_aut'] = self.request.user.groups.exists()
        return context


class CityBusDetail(DetailView):
    template_name = 'city_bus_detail.html'
    context_object_name = 'bus_detail'
    queryset = RoutesCity.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_aut'] = self.request.user.groups.exists()
        return context


class RoutesAddView(CreateView):
    model = RoutesCity
    template_name = 'create.html'
    form_class = RoutesCityForm


class RoutesUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = RoutesCityForm # Форму берём ту же что и для добавления новых данных

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return RoutesCity.objects.get(pk=id)


class RoutesDeleteView(DeleteView):
    context_object_name = 'routes'
    template_name = 'delete_routes.html'
    queryset = RoutesCity.objects.all()
    success_url = '/bus/city_bus/'


class NewsAddView(CreateView):
    model = News
    template_name = 'create.html'
    form_class = NewsForm


class NewsUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = NewsForm # Форму берём ту же что и для добавления новых данных

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    context_object_name = 'news'
    template_name = 'delete_news.html'
    queryset = News.objects.all()
    success_url = '/bus/'


class VacanciesAddView(CreateView):
    model = Vacancies
    template_name = 'create.html'
    form_class = VacanciesForm


class VacanciesUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = VacanciesForm # Форму берём ту же что и для добавления новых данных

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Vacancies.objects.get(pk=id)


class VacanciesDeleteView(DeleteView):
    context_object_name = 'vacanci'
    template_name = 'delete_vacancies.html'
    queryset = Vacancies.objects.all()
    success_url = '/bus/vacancies'