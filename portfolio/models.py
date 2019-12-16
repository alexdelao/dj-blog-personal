from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField('Titulo', max_length=250)
    description = models.TextField('Descripcion')
    link = models.URLField('Enlace', max_length=200)
    image = models.ImageField('Imagen', upload_to='portfolio')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edicion')

    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
