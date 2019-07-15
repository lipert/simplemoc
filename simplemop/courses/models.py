from django.db import models

class CourseManager(models.Manager):
    def search(self,query):

        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )


class Courses(models.Model):
    name = models.CharField('Nome',max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descricao')
    start_date = models.DateField(
        'Data Inicio',blank=True,null=True)
    image = models.ImageField(
        upload_to = 'courses/images',verbose_name = 'Imagem',blank=True,null=True
    )
    created_at = models.DateTimeField(
        'Criado em', auto_now_add = True,blank=True,null=True
        )

    upload_at = models.DateTimeField('Atualizado em', auto_now = True,blank=True,null=True)
    objects = CourseManager()

    def __str__(self):
        return self.name

        


