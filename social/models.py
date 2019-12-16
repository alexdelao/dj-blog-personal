from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField('clave', max_length=200, unique=True)
    name = models.CharField('Nombre', max_length=200)
    url = models.URLField('Enlace', max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edicion')

    
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.name