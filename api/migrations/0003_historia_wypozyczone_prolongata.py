# Generated by Django 5.0.4 on 2024-05-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_wypozyczone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uzytkownik', models.CharField(blank=True, max_length=32)),
                ('autor', models.CharField(blank=True, max_length=64)),
                ('tytul', models.CharField(blank=True, max_length=256)),
                ('opis', models.CharField(blank=True, max_length=256)),
                ('datawypoz', models.DateField(blank=True)),
                ('datazwrotu', models.DateField(blank=True)),
                ('ulubione', models.BooleanField(default=False)),
                ('notatki', models.CharField(blank=True, max_length=256)),
                ('prolongata', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='wypozyczone',
            name='prolongata',
            field=models.BooleanField(default=False),
        ),
    ]
