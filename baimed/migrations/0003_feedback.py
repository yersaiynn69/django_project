# Generated by Django 4.2.6 on 2023-11-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baimed', '0002_aboutme_alter_product_price_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('email', models.CharField(max_length=100, verbose_name='Описание')),
                ('message', models.TextField(blank=True, verbose_name='Контент')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
                'ordering': ['time_create'],
            },
        ),
    ]
