from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    fullname = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    biographies =models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    def _str_(self) -> str:
        return self.fullname