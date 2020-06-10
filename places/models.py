from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200, blank=True)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Подробное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return f'{self.title}'