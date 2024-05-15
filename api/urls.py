
from django.contrib import admin

from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'ksiazki', views.KsiazkaViewSet, basename='Ksiazka')
router.register(r'wypozyczone', views.WypozyczoneViewSet)
router.register(r'historia', views.HistoriaViewSet)




urlpatterns = [
    path('', include(router.urls)),

]