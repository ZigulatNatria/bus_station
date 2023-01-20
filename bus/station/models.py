from django.db import models


# Create your models
class Routes(models.Model):
    name = models.CharField(max_length=20)

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

# class BusRoutes(models.Model):
#     bus_rouets = models.ForeignKey(Bus, on_delete=models.CASCADE)
#     routes_bus = models.ForeignKey(Routes, on_delete=models.CASCADE)


class Vacancies(models.Model):
    vacancies_img = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')
    name = models.CharField(max_length=100)
    info = models.TextField()

    class Meta:
        verbose_name_plural = 'Вакансия'
        verbose_name = 'Вакансии'


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    info_gallery = models.TextField()
    cover_gallery = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')

    class Meta:
        verbose_name_plural = 'Альбом'
        verbose_name = 'Альбомы'


class Photo(models.Model):
    image = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')
    photoGallery = models.ForeignKey('Gallery', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Фотография'
        verbose_name = 'Фотографии'

class News(models.Model):
    news_header = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    image = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')

    def __str__(self):
        return '{}'.format(self.news_header) #TODO перепилить на все модели


class RoutesCity(models.Model):
    number = models.CharField(max_length=20)
    track = models.CharField(max_length=100)
    image_route = models.ImageField(null=True, width_field=None, height_field=None, upload_to='images/')

