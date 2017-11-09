from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from auth.serializers import UserSerializer
from patient.models import PatientData


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PatientData.objects.all()
    serializer_class = UserSerializer