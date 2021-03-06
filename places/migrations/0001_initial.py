# Generated by Django 3.0.4 on 2020-06-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Название')),
                ('description_short', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('description_long', models.TextField(blank=True, verbose_name='Подробное описание')),
                ('lng', models.FloatField(verbose_name='Долгота')),
                ('lat', models.FloatField(verbose_name='Широта')),
            ],
        ),
    ]
