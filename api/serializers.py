from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Ksiazka, Wypozyczone, Historia

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = ['id', 'autor', 'tytul', 'opis', 'stan']

class WypozyczoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczone
        fields = ['id', 'uzytkownik', 'autor', 'tytul', 'opis', 'datawypoz', 'czyoddane', 'ulubione', 'notatki', 'prolongata']


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['id', 'uzytkownik', 'autor', 'tytul', 'opis', 'datawypoz', 'datazwrotu', 'ulubione', 'notatki', 'prolongata']