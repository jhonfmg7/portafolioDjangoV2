from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.

class Instagram(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(verbose_name="Imagenes de Instagram", upload_to="Instagram", blank=True, null=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(verbose_name='Titulo de texto', max_length=200, blank=True, null=True)
    content = RichTextField(verbose_name='Contenido de texto', max_length=1000, blank=True, null=True)
    content_2 = RichTextField(verbose_name='Contenido de texto', max_length=1000, blank=True, null=True)
    url = models.URLField(verbose_name="Url del video", max_length=200)
    image = models.ImageField(verbose_name="Imagen video", upload_to="video", blank=True, null=True)

class Video_2(models.Model):
    title = models.CharField(verbose_name='Titulo de texto', max_length=200, blank=True, null=True)
    content = RichTextField(verbose_name='Contenido de texto', max_length=1000, blank=True, null=True)
    content_2 = RichTextField(verbose_name='Contenido de texto', max_length=1000, blank=True, null=True)
    url = models.URLField(verbose_name="Url del video", max_length=200)
    image = models.ImageField(verbose_name="Imagen video", upload_to="video", blank=True, null=True)

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    career = models.CharField(max_length=100, verbose_name="Profesión")
    image = models.ImageField(verbose_name='Imagen team', blank=True, null=True, upload_to='team')
    facebook = models.URLField(verbose_name="facebook", max_length=200, blank=True, null=True)
    twitter = models.URLField(verbose_name="twitter", max_length=200, blank=True, null=True)
    linkedin = models.URLField(verbose_name="linkedin", max_length=200, blank=True, null=True)
    another = models.CharField(verbose_name="another", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Choose(models.Model):
    icon = models.CharField(verbose_name="Icono", max_length=20)
    title = models.CharField(verbose_name="Titulos de la elección", max_length=100)
    content = RichTextField(verbose_name="Descripción de la elección", max_length=300)

    class Meta:
        verbose_name="Elección"
        verbose_name_plural="Elecciones"

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    type_service = models.CharField(max_length=200, verbose_name="tipo")

    def __str__(self):
        return self.title
    

class Ability(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripcion de la habilidad", blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    percentage_reverse = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100, verbose_name="Color", default='color-1')
    
    class Meta:
        verbose_name="Halilidad"
        verbose_name_plural="Habilidades"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    title = models.CharField(max_length=100, verbose_name="Titulo", blank=True, null=True)
    filter_search = models.CharField(max_length=100, verbose_name="Filtro", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(verbose_name="Titulo de la Foto", max_length=100)
    image = models.URLField(verbose_name="Imagen", null=True, blank=True)
    description = RichTextField(verbose_name="Descripción de la foto", max_length=300)
    tags = models.ManyToManyField(Tag, verbose_name="Etiquetas")
    delay =  models.CharField(max_length=100, blank=True, null=True, default="100ms")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Imagen de Lugares"
        verbose_name_plural = "Imagenes de Lugares"

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    image1 = models.ImageField(verbose_name="Imagen uno", upload_to="Projects", null=True, blank=True)
    image2 = models.ImageField(verbose_name="Imagen dos", upload_to="Projects", null=True, blank=True)
    content = RichTextField(verbose_name="Contenido")
    relevance = models.IntegerField(verbose_name='Importancia', default=0)
    role = models.ManyToManyField(Category, verbose_name="Categorías")
    comment = models.CharField(verbose_name="Comentario", max_length=200)
    author_comment = models.CharField(verbose_name="autor", max_length=100)
    author_image = models.ImageField(verbose_name="Imagen Autor", upload_to="Projects/author", null=True, blank=True)
    date_start = models.DateTimeField(verbose_name="Fecha de Inicio", default=now)
    date_end = models.DateTimeField(verbose_name="Fecha de Finalización", default=now)
    url = models.URLField(verbose_name="URL", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Achievements(models.Model):
    title = models.CharField(verbose_name="logros", max_length=300)
    relation = models.CharField(verbose_name="carrera", max_length=200)

    def __str__(self):
        return self.relation

class Career(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, null=True, blank=True)
    important_title = models.CharField(verbose_name="Titulo Importante", max_length=200, null=True, blank=True)
    institution = models.CharField(verbose_name="Institución", max_length=200)
    achievements = models.ManyToManyField(Achievements, verbose_name="logros")
    place = models.CharField(verbose_name="Lugar", max_length=200, null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="Career", null=True, blank=True)
    session = models.CharField(verbose_name="Sesión", max_length=100)
    date_start = models.DateTimeField(verbose_name="Fecha de Inicio", default=now)
    date_end = models.DateTimeField(verbose_name="Fecha de Finalización", default=now)
    result = models.FloatField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carrera"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=200)
    phone = models.CharField(verbose_name="Numero de Contacto", max_length=100)
    fijo = models.CharField(verbose_name="Numero de Contacto", max_length=100, default=0)

    def __str__(self):
        return self.email
    
    
