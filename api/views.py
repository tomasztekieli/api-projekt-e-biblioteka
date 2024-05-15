from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import filters
from api.serializers import UserSerializer
from .models import Ksiazka, Wypozyczone, Historia
from .serializers import KsiazkaSerializer, WypozyczoneSerializer, HistoriaSerializer
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class KsiazkaViewSet(viewsets.ModelViewSet):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['autor', 'tytul', 'opis']
    permission_classes = [permissions.AllowAny]



    @action(detail=True)
    def nowystan(self, request, **kwargs):
        ksiazka = self.get_object()
        ksiazka.stan = ksiazka.stan - 1
        ksiazka.save()

        serializer = KsiazkaSerializer(ksiazka, many=False)
        return Response(serializer.data)

class WypozyczoneViewSet(viewsets.ModelViewSet):
    queryset = Wypozyczone.objects.all()
    serializer_class = WypozyczoneSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True)
    def ulubione(self, request, **kwargs):
        wypozyczone= self.get_object()
        wypozyczone.ulubione = True
        wypozyczone.save()

        serializer = WypozyczoneSerializer(wypozyczone, many=False)
        return Response(serializer.data)

    @action(detail=True)
    def ulubioneoff(self, request, **kwargs):
        wypozyczone= self.get_object()
        wypozyczone.ulubione = False
        wypozyczone.save()

        serializer = WypozyczoneSerializer(wypozyczone, many=False)
        return Response(serializer.data)

    @action(detail=True)
    def prolonguj(self, request, **kwargs):
        wypozyczone = self.get_object()
        wypozyczone.prolongata = True
        wypozyczone.save()

        serializer = WypozyczoneSerializer(wypozyczone, many=False)
        return Response(serializer.data)

class HistoriaViewSet(viewsets.ModelViewSet):
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True)
    def ulubioneoff(self, request, **kwargs):
        historia = self.get_object()
        historia.ulubione = False
        historia.save()

        serializer = WypozyczoneSerializer(historia, many=False)
        return Response(serializer.data)