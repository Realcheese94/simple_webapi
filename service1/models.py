# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Animal(models.Model):
    animal_name = models.CharField(max_length=10)
    animal_size = models.CharField(max_length=5)
