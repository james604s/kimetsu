# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from utils.iconst import *

class MaskData(models.Model):
    num_child = models.IntegerField(blank=True, null=True)
    num_adult = models.IntegerField(blank=True, null=True)
    agency_phone = models.CharField(max_length=100, blank=True, null=True)
    agency_name = models.CharField(max_length=100, blank=True, null=True)
    agency_code = models.CharField(max_length=100, blank=True, null=True)
    agency_address = models.CharField(max_length=100, blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True, choices=CITY_CHOICES)

    class Meta:
        managed = False
        db_table = 'mask_data'

