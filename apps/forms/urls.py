from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterFormClientView, LoanFormClientView, Dashboard
from .viewSets import RegisterFormViewSet, LoanFormViewSet

router = DefaultRouter()
router.register('requests', RegisterFormViewSet)
router.register('loans', LoanFormViewSet)

urlpatterns = [
    path('client/register/request', RegisterFormClientView.as_view()),
    path('client/loan/request', LoanFormClientView.as_view()),
    path('dashboard', Dashboard.as_view()),
    path('', include(router.urls)),
]
