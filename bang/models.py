
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.CharField(max_length=255, blank=True, verbose_name='Цена')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['time_create', 'title']


class AboutMe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.CharField(max_length=100, verbose_name='Описание')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О себе'
        verbose_name_plural = 'О себе'
        ordering = ['title']


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    email = models.CharField(max_length=100, verbose_name='Описание')
    message = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['time_create']
