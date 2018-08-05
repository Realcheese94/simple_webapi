# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Person,Animal,Persondetail
from .serializers import  PersonSerializers,AnimalSerializers,PersondetailSerializers
from rest_framework import viewsets


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

class AnimalViewset(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializers

class PersondatailViewSet(viewsets.ModelViewSet):
    queryset = Persondetail.objects.all()
    serializer_class = PersondetailSerializers
# Create your views here.
