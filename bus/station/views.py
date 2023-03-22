from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from .models import Routes, Bus, Vacancies, Gallery, Photo, News, RoutesCity, Contacts, \
    PhotoCarusel, History, Insurer, Service, ForPassengers, BestEmployee, Information #BusRoutes
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

    @staticmethod       # Применяем декоратор для функции вызова по второй модели
    def all_images():   # (в шаблоне обращаться view.all_images)
        photo = list(PhotoCarusel.objects.all())  # Формируем список из всех фото кроме первого
        current_photo = photo[1:]
        return current_photo

    @staticmethod
    def first_images():    # Забираем только первое фото (нужно для старта карусели)
        return PhotoCarusel.objects.all().first()


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
    return render(request, 'by_galleries3.html', context)


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
                          ['ZigulatNatria@yandex.ru'])
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
        vacancies = Vacancies.objects.filter(name__icontains=search_query)
    else:
        news = News.objects.all()
        vacancies = Vacancies.objects.all()
    context = {'news': news,
               'vacancies': vacancies
               }
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


class RoutesAddView(PermissionRequiredMixin, CreateView):
    permission_required = ('station.add_routescity')
    model = RoutesCity
    template_name = 'create.html'
    form_class = RoutesCityForm


class RoutesUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('station.change_routescity')
    template_name = 'create.html'
    form_class = RoutesCityForm # Форму берём ту же что и для добавления новых данных

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return RoutesCity.objects.get(pk=id)


class RoutesDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('station.delete_routescity')
    context_object_name = 'routes'
    template_name = 'delete_routes.html'
    queryset = RoutesCity.objects.all()
    success_url = '/bus/city_bus/'


class NewsAddView(PermissionRequiredMixin, CreateView):
    permission_required = ('station.add_news')
    model = News
    template_name = 'create.html'
    form_class = NewsForm


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('station.change_news')
    template_name = 'create.html'
    form_class = NewsForm # Форму берём ту же что и для добавления новых данных

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('station.delete_news')
    context_object_name = 'news'
    template_name = 'delete_news.html'
    queryset = News.objects.all()
    success_url = '/bus/'


class VacanciesAddView(PermissionRequiredMixin, CreateView):
    permission_required = ('station.add_vacancies')
    model = Vacancies
    template_name = 'create.html'
    form_class = VacanciesForm


class VacanciesUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('station.change_vacancies')
    template_name = 'create.html'
    form_class = VacanciesForm # Форму берём ту же что и для добавления новых данных

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Vacancies.objects.get(pk=id)


class VacanciesDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('station.delete_vacancies')
    context_object_name = 'vacanci'
    template_name = 'delete_vacancies.html'
    queryset = Vacancies.objects.all()
    success_url = '/bus/vacancies'


class ContactsListView(ListView):
    model = Contacts
    context_object_name = 'contacts'
    template_name = 'contacts.html'
    queryset = Contacts.objects.all()


class HistoryListView(ListView):
    model = History
    context_object_name = 'history'
    template_name = 'history.html'
    queryset = History.objects.all()


class InsurerListView(ListView):
    model = Insurer
    context_object_name = 'insurer'
    template_name = 'insurer.html'
    queryset = Insurer.objects.all()


class ServiceListView(ListView):
    model = Service
    context_object_name = 'service'
    template_name = 'service.html'
    queryset = Service.objects.all()


class ForPassengersListView(ListView):
    model = ForPassengers
    context_object_name = 'for_passengers'
    template_name = 'for_passengers.html'
    queryset = ForPassengers.objects.all()


class BestEmployeeListView(ListView):
    model = BestEmployee
    context_object_name = 'best_employee'
    template_name = 'best_employee.html'
    queryset = BestEmployee.objects.all()


class InformationListView(ListView):
    model = Information
    context_object_name = 'information'
    template_name = 'information.html'
    queryset = Information.objects.all()