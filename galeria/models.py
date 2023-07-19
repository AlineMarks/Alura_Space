from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ('GALÁXIA','Galáxia'),
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('PLANETA', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, blank=False, null=False)
    legenda = models.CharField(max_length=150, blank=False,null=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA ,default='')
    descricao = models.TextField(blank=False,null=False)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"{self.nome}"
