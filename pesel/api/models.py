from django.db import models


class Pesel(models.Model):
    pesel = models.CharField(max_length=11)
    valid = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.pesel

class Moods(models.Model):
    nazwa = models.CharField(max_length=100)
    wartosc_samopoczucia = models.IntegerField()

    def __str__(self):
        return self.nazwa


class ActualMood(models.Model):
    nazwa = models.CharField(max_length=100)
    wartosc_samopoczucia = models.IntegerField()

    def __str__(self):
        return self.nazwa