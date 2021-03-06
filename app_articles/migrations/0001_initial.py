# Generated by Django 2.0.5 on 2019-12-09 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('published_at', models.DateTimeField(verbose_name='Дата публикации')),
                ('image', models.CharField(blank=True, max_length=128, null=True, verbose_name='Изображение')),
                ('slug', models.SlugField(max_length=100)),
                ('products', models.ManyToManyField(blank=True, to='app_eshop.Product', verbose_name='Продукты')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eshop.Section')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
