from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class tasks(models.Model):
    name = models.CharField(max_length=20)
    money = models.SlugField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name + str(self.money) + str(self.completed)

