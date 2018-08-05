# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import  Person,Animal

class PersonSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id','first_name','last_name')

class AnimalSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"