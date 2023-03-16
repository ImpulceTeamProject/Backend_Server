from django.db import models


# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    date_of_birth = models.DateField()
    avatar = models.ImageField(upload_to='avatars', verbose_name='Аватар')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Электронная почта')
    vk_link = models.CharField(max_length=100, verbose_name='Ссылка на ВК')
    instagram_link = models.CharField(max_length=100, verbose_name='Ссылка на Instagram')
    telegram_link = models.CharField(max_length=100, verbose_name='Ссылка на Telegram')

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}"
