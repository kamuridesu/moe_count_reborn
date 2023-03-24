from django.db import models

# Create your models here.

class User(models.Model):
    name: str = models.CharField(max_length=255)
    count: int = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name}: {self.count}"
