# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Job(models.Model):
    imagen= models.ImageField(upload_to='images')
    descripcion = models.CharField(max_length=200)
