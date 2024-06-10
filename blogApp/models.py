from django.db import models

#Se define la clase para articulos.
class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    categoria = models.ManyToManyField('Categoria' )
    contenido = models.TextField()
    imagen_principal = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    imagen_secundaria = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    imagen_terciaria = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    video_principal = models.URLField(blank=True, null=True)
    video_secundario = models.URLField(blank=True, null=True)
    video_terciario = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
#Se define la clase para categorias.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
