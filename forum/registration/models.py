from django.db import models


class Participants(models.Model):
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    company = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=30, blank=False)
    tel = models.IntegerField(blank=False)
    address = models.EmailField(blank=False)



class Good(models.Model):
    theme = models.CharField(max_length=238, blank=True)
    theme_extended = models.CharField(max_length=238, blank=True)
    detail_description = models.TextField()

    # name_good = models.CharField(max_length=30, unique=True, blank=True)
    # data_add = models.DateField(auto_now=True)

    def __str__(self):
        return self.detail_description, self.theme, self.theme_extended


