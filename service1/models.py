# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class PersonInfo(models.Model):
    person_no = models.ForeignKey(Person)
    person_height = models.CharField(max_length=10)
    person_weight = models.CharField(max_length=10)
