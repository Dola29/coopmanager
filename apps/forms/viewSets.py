from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND

from .models import RegisterForm, LoanForm
from .serializers import RegisterFormSerializer, LoanFormSerializer

class RegisterFormViewSet(ModelViewSet):
    serializer_class = RegisterFormSerializer
    queryset = RegisterForm.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','lastname','dob')

class LoanFormViewSet(ModelViewSet):
    serializer_class = LoanFormSerializer
    queryset = LoanForm.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','lastname','dob','cedula')