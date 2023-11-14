from django.db import models

class Article(models.Model):

    name = models.CharField(max_length=250)
    age = models.FloatField()
    gender = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    ap_hi = models.FloatField()
    ap_lo = models.FloatField()
    cholesterol = models.FloatField()
    gluc = models.FloatField()
    smoke = models.FloatField()
    alco = models.FloatField()
    active = models.FloatField()
    cardio = models.FloatField()
    bp_category = models.FloatField()


