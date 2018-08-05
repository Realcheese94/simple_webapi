# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import  Person,Animal,Persondetail

class PersonSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id','first_name','last_name')

class AnimalSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"

class PersondetailSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persondetail
        fields ="__all__"