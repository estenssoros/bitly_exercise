from __future__ import unicode_literals

from django.db import models


class Block(models.Model):
    id = models.IntegerField(primary_key=True)
    start_ip_num = models.IntegerField()
    end_ip_num = models.IntegerField()
    loc_id = models.IntegerField()

    class Meta:
        db_table = 'blocks'
        verbose_name = 'Block'
        verbose_name_plural = 'Blocks'


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    loc_id = models.IntegerField()
    country = models.CharField(max_length=2, blank=True, null=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=48, blank=True, null=True)
    postal_code = models.CharField(max_length=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    metro_code = models.IntegerField()
    area_code = models.IntegerField()

    class Meta:
        db_table = 'location'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
