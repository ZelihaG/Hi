from django.db import models
class Instrument(models.Model):
    enst_name = models.CharField(max_length=30)

