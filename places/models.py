from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200, blank=True)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Подробное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, verbose_name='Место локации', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Картинка', blank=True)

    def __str__(self):
        return self.id, self.place.title