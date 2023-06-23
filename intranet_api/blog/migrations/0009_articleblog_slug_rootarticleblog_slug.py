# Generated by Django 4.1.5 on 2023-06-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_rootarticleblog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleblog',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='rootarticleblog',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Slug'),
        ),
    ]