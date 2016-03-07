# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.db.backends.mysql.validation import DatabaseValidation

class Machine(models.Model):
    mac = models.CharField(db_column='MAC', max_length=17, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=32)  # Field name made lowercase.
    salle = models.IntegerField(db_column='SALLE')  # Field name made lowercase.
    num = models.AutoField(primary_key=True)
    type_connect = models.IntegerField(blank=True, null=True)
    type_os = models.IntegerField(blank=True, null=True)
    vm_audio = models.IntegerField(db_column='vm_audio', blank=True, null=True)
    type_poste = models.CharField(db_column='TYPE_POSTE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(max_length=64, blank=True, null=True)
    pyddlaj = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom
    
    class Meta:
        managed = False
        db_table = 'MACHINE'
