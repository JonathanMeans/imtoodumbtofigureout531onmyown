# Create your models here.
from django.db import models


class Lift(models.Model):
    name = models.CharField(max_length=100)
    training_max = models.IntegerField()
    week_number = models.IntegerField()

    @property
    def url(self) -> str:
        return f"/lift?training_max={self.training_max}&week_number={self.week_number}"
