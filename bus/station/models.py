from django.db import models
from tinymce.models import HTMLField
from PIL import Image #импорт из PILLOW для обращения к изображению


# Create your models
class Routes(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Маршрут'

    def __str__(self):
        return '{}'.format(self.name)


class Bus(models.Model):
    routes = models.ForeignKey(Routes, on_delete=models.CASCADE)
    # start_place = models.CharField(max_length=20)
    # finish_place = models.CharField(max_length=20)
    time_start = models.CharField(max_length=5) #заменить на поле время
    time_finish = models.CharField(max_length=5) #заменить на поле время
    day_finish = models.CharField(max_length=8) #заменть на поле даты
    day_start = models.CharField(max_length=8)  #заменть на поле даты
    number_bus = models.CharField(max_length=10)
    cost = models.IntegerField(null=True)
    trevel_time = models.CharField(max_length=10, null=True)

    def __str__(self):
        return 'Автобус маршрута' + ' ' + '{}'.format(self.routes)

    class Meta:
        verbose_name = 'Автобус'

# class BusRoutes(models.Model):
#     bus_rouets = models.ForeignKey(Bus, on_delete=models.CASCADE)
#     routes_bus = models.ForeignKey(Routes, on_delete=models.CASCADE)


class Vacancies(models.Model):
    vacancies_img = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')
    name = models.CharField(max_length=100)
    info = models.TextField()

    # Функция для преобразования загружаемой картинки к нужному размеру
    # def save(self):
    #     super().save()
    #     img = Image.open(self.vacancies_img.path)
    #     resized_image = img.resize((320, 320), reducing_gap=1.1)
    #     resized_image.save(self.vacancies_img.path)

    # def save(self):
    #     super().save()
    #     img = Image.open(self.vacancies_img.path)
    #     fixed_height = 1000
    #     height_percent = (fixed_height / float(img.size[1]) )
    #     width_size = int((float(img.size[1]) * float(height_percent)))
    #     img = img.resize((fixed_height, width_size))
    #     img.save(self.vacancies_img.path)

    class Meta:
        verbose_name_plural = 'Вакансия'
        verbose_name = 'Вакансии'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/vacancies'


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    info_gallery = models.TextField()
    cover_gallery = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')

    class Meta:
        verbose_name_plural = 'Альбом'
        verbose_name = 'Альбомы'

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')
    photoGallery = models.ForeignKey('Gallery', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Фотография'
        verbose_name = 'Фотографии'

    def __str__(self):
        return 'Фотография альбома' + ' ' + '{}'.format(self.photoGallery)

class News(models.Model):
    news_header = models.CharField(max_length=100, null=True)
    text = HTMLField()
    image = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')
    file = models.FileField(verbose_name='Файл', upload_to='media', null=True, blank=True)

    class Meta:
        verbose_name = 'Новости'
        ordering = ['-id']

    def __str__(self):
        return '{}'.format(self.news_header) #TODO перепилить на все модели

    def get_absolute_url(self):
        return f'/'


# class News(models.Model):
#     news_header = models.CharField(max_length=100, null=True)
#     text = models.TextField(null=True)
#     image = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')
#
#     class Meta:
#         verbose_name = 'Новости'
#
#     def __str__(self):
#         return '{}'.format(self.news_header) #TODO перепилить на все модели


class Contacts(models.Model):
    director = models.CharField(max_length=100, verbose_name='ФИО руководителя', null=True, blank=True)
    basis = models.TextField(verbose_name='На основании какого документа действет', null=True, blank=True)
    accountant = models.CharField(max_length=100, verbose_name='ФИО главного бухгалтера', null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name='Телефон/факс', null=True, blank=True)
    address = models.TextField(verbose_name='Адрес', null=True, blank=True)
    mail = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    inn = models.CharField(max_length=100, verbose_name='ИНН', null=True, blank=True)
    checking_account = models.CharField(max_length=100, verbose_name='Расчётный счёт', null=True, blank=True)
    correspondent_account = models.CharField(max_length=100, verbose_name='Корреспондентский счёт', null=True, blank=True)
    bik = models.CharField(max_length=100, verbose_name='БИК', null=True, blank=True)
    recipient = models.TextField(verbose_name='Получатель', null=True, blank=True)
    okpo = models.CharField(max_length=100, verbose_name='ОКПО', null=True, blank=True)
    okogu = models.CharField(max_length=100, verbose_name='ОКОГУ', null=True, blank=True)
    okato = models.CharField(max_length=100, verbose_name='ОКАТО', null=True, blank=True)
    okved = models.CharField(max_length=100, verbose_name='ОКВЭД', null=True, blank=True)
    ogrn = models.CharField(max_length=100, verbose_name='ОГРН', null=True, blank=True)
    bus_station_address = models.TextField(verbose_name='Адресс автовокзала', null=True, blank=True)
    bus_station_phone = models.TextField(verbose_name='Телефон касс автовокзала', null=True, blank=True)

    class Meta:
        verbose_name = 'Контакты'

    def __str__(self):
        return 'Контакты'
    
    
class PhotoCarusel(models.Model):
    images = models.ImageField(verbose_name='фото')

    # Функция для преобразования загружаемой картинки к нужному размеру
    # def save(self):
    #     super().save()
    #     img = Image.open(self.images.path)
    #     fixed_height = 800
    #     height_percent = (fixed_height / float(img.size[1]) )
    #     width_size = int((float(img.size[1]) * float(height_percent)))
    #     img = img.resize((fixed_height, width_size))
    #     img.save(self.images.path)

    class Meta:
        verbose_name = 'Фотографии главной страницы'

    def __str__(self):
        return 'Фото' + ' ' + '{}'.format(self.id)


class RoutesCity(models.Model):
    number = models.CharField(max_length=20)
    track = models.CharField(max_length=100)
    content = HTMLField()

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Городские маршруты'

    def get_absolute_url(self):

        return f'/city_bus/'


class History(models.Model):
    text = HTMLField(verbose_name='Текст', null=True, blank=True)

    class Meta:
        verbose_name = 'Текст про компанию'

    def __str__(self):
        return 'Текст' + ' ' + '{}'.format(self.id)


class Insurer(models.Model):
    text = HTMLField(verbose_name='Текст', null=True, blank=True)

    class Meta:
        verbose_name = 'О страховщиках'

    def __str__(self):
        return 'О страховщиках' + ' ' + '{}'.format(self.id)


class Service(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=200)
    text = HTMLField(verbose_name='Текст', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='media', null=True, blank=True)

    class Meta:
        verbose_name = 'Услуги'

    def __str__(self):
        return 'Услуга' + ' ' + '{}'.format(self.name)


class ForPassengers(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=200)
    text = HTMLField(verbose_name='Текст', null=True, blank=True)

    class Meta:
        verbose_name = 'Для пассажиров'

    def __str__(self):
        return 'Для пассажиров' + ' ' + '{}'.format(self.name)


class BestEmployee(models.Model):
    name = models.CharField(verbose_name='Имя работника', max_length=100)
    photo = models.ImageField(verbose_name='Фотография')
    profession = models.CharField(verbose_name='профессия', max_length=200, null=True, blank=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)

    class Meta:
        verbose_name = 'Лучшие работники'

    def __str__(self):
        return self.name


class Information(models.Model):
    name = models.CharField(verbose_name='Название документа', max_length=100)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='media', null=True, blank=True)

    class Meta:
        verbose_name = 'Уставные документы'

    def __str__(self):
        return self.name


class Timetable(models.Model):
    name = models.CharField(verbose_name='Название блока', max_length=100)
    text = models.TextField(verbose_name='Описание блока')
    file = models.FileField(verbose_name='Файл', upload_to='media', null=True, blank=True)
    link = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    image = models.ImageField(verbose_name='Фотография')

    class Meta:
        verbose_name = 'Расписания'
        ordering = ['-id']

    def get_absolute_url(self):
        return f'/timetable/'

    def __str__(self):
        return self.name