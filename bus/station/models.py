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
#
class Vacancies(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()

