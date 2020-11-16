from django.db import models


class Tulkkaa(models.Model):
    kielikoodi = models.CharField(max_length=2)
    kielinimi = models.CharField(max_length=25)
    fkieli = models.BooleanField(default=True)
    tkieli = models.BooleanField(default=True)
    lippu = models.FileField()

    def __str__(self):
        return self.kielinimi
