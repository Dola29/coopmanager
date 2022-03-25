from django.db import router
from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView
from .viewsSets import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login', LoginView.as_view()),
    path('auth/user', UserView.as_view()),
    path('auth/logout', LogoutView.as_view()),
    path('', include(router.urls)),
]
