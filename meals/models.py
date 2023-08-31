from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    fat = models.DecimalField(verbose_name="Fat")
    carbs = models.DecimalField(verbose_name="Carbohydrates")
    protein = models.DecimalField(verbose_name="Protein")
