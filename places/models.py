from django.db import models


class Place(models.Model):
    title = models.CharField('название', max_length=200)

    def __str__(self):
        return f'{self.title}'