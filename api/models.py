from django.db import models
from datetime import date

class Ksiazka(models.Model):
    autor = models.CharField(max_length=64)
    tytul = models.CharField(max_length=256)
    opis = models.CharField(max_length=256)
    stan = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.tytul

class Wypozyczone(models.Model):
    uzytkownik = models.CharField(max_length=32, blank=True)
    autor = models.CharField(max_length=64, blank=True)
    tytul = models.CharField(max_length=256, blank=True)
    opis = models.CharField(max_length=256, blank=True)
    datawypoz = models.DateField(default=date.today)
    czyoddane = models.BooleanField(default=False)
    ulubione = models.BooleanField(default=False)
    notatki = models.CharField(max_length=256, blank=True)
    prolongata = models.BooleanField(default=False)
    def __str__(self):
        return self.tytul

class Historia(models.Model):
    uzytkownik = models.CharField(max_length=32, blank=True)
    autor = models.CharField(max_length=64, blank=True)
    tytul = models.CharField(max_length=256, blank=True)
    opis = models.CharField(max_length=256, blank=True)
    datawypoz = models.DateField(blank=True)
    datazwrotu = models.DateField(blank=True)
    ulubione = models.BooleanField(default=False)
    notatki = models.CharField(max_length=256, blank=True)
    prolongata = models.BooleanField(default=False)

    def __str__(self):
        return self.tytul