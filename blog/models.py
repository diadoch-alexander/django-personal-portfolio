from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200,verbose_name='Название блога')
    description=models.TextField(verbose_name="Текст блога")
    date=models.DateField(verbose_name='Дата публикации')

    def __str__(self):
        return f'Блог номер: {self.id}'