from posixpath import split
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from .models import RegisterForm, LoanForm
import json
from django.db.models import Count
from django.db.models.functions import TruncMonth
from .helpers import get_arr



from .serializers import RegisterFormSerializer, LoanFormSerializer

class RegisterFormClientView (APIView):
    def post(self, request):
        serializer = RegisterFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

class LoanFormClientView (APIView):
    def post(self, request):
        serializer = LoanFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

class Dashboard (APIView):
    def get(self, request):
        registerLine = get_arr(RegisterForm.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).values('month', 'count'))
        loanLine = get_arr(LoanForm.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).values('month', 'count'))
        regiserCount = RegisterForm.objects.count()
        loanCount = LoanForm.objects.count()

        data ={
            "register_line":registerLine,
            "loan_line":loanLine,
            "register_count":regiserCount,
            "loan_count":loanCount
        }
        return Response(data , status=HTTP_200_OK)

   



