from django.db import models

# Create your models here.
class Cancion(models.Model):
    id=models.IntegerField(
        primary_key=True
    )
    nombre=models.CharField(
        max_length=50,
        help_text='nombre de la cancion',   
    )
    autor=models.CharField(
        max_length=100,
        help_text='Quien escribio la cancion'
    )
    def __str__(self):
        return f"{self.nombre} fue escrita {self.autor}"
    class Meta:
        verbose_name_plural="Canciones"