# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Lift(models.Model):
    name = models.CharField(max_length=100, blank=True, default="")
    training_max = models.FloatField()
    week_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )

    @property
    def url(self) -> str:
        return f"/lift?id={self.id}"
