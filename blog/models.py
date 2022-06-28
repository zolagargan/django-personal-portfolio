from django.db import models
from django.forms import CharField, DateTimeField

class Blog(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateTimeField()
    description = models.TextField(max_length=1000)

    # Функция для отображения названия объекта в админке
    def __str__(self):
        return self.title 