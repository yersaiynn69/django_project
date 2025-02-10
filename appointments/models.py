from django.urls import reverse
from django.db import models



class Appointments(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Пациент записан'),
        ('completed', 'Приём выполнен'),
        ('cancelled', 'Приём отменён'),
    ]
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    organisation = models.CharField(max_length=255, verbose_name='Организация')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='scheduled',
        verbose_name='Статус'
    )
    service_type = models.CharField(max_length=255, verbose_name='Услуга')



    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return reverse('show_appointment', kwargs={'appointment_slug': self.slug})

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['time_create', 'title']