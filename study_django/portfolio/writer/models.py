from django.db import models

# Create your models here.
from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  # Потребуется настройка для работы с изображениями
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

