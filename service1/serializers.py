# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import  Person

class PersonSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id','first_name','last_name')
