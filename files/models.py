from __future__ import unicode_literals

from django.db import models
from s3direct.fields import S3DirectField

class Upload(models.Model):
    custom_filename = S3DirectField(dest='custom_filename', blank=True)

class File(models.Model):
    up_file = models.ForeignKey('Upload')
    upload = S3DirectField(dest='misc', blank=True)

class Meta(models.Model):
    filename = models.CharField(max_length=128)
    size = models.IntegerField()
    upload_date = models.DateTimeField()
    user = models.CharField(max_length=128)

class Data(models.Model):
    title = models.CharField(max_length=128, null=True)
    author = models.CharField(max_length=128, null=True)
    #publisher = models.CharField(max_length=128)
    #publication_date = models.DateField()
    #citations = models.IntegerField()

