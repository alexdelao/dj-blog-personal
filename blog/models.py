from django.db import models
from django.utils.timezone import now     
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    title = models.CharField('Titulo', max_length=200)
    subtitle = models.CharField('Subtitulo', max_length=200)
    content = RichTextUploadingField('Contenido')
    image = models.ImageField('Imagen', upload_to='blog')
    published = models.DateTimeField(verbose_name='fecha publicacion',default=now)
    author= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edicion')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')


    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title
        
