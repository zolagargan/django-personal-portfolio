from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) 
    
    # Функция для отображения названия объекта в админке
    def __str__(self):
        return self.title 