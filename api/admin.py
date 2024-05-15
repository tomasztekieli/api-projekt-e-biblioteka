from django.contrib import admin
from .models import Ksiazka, Wypozyczone, Historia

admin.site.register(Ksiazka)
admin.site.register(Wypozyczone)
admin.site.register(Historia)
