from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.CharField(max_length=100, verbose_name='Description')
    content = models.TextField(blank=True, verbose_name='Content')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
        ordering = ['title']
