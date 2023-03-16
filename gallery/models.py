from django.db import models


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', default='')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    small_image = models.ImageField(upload_to='images', verbose_name='Уменьшенное изображение', default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.title


