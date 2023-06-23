# Generated by Django 4.1.5 on 2023-06-23 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_articleblog_categoryblog_delete_article_blog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RootCategoryBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Root category',
                'verbose_name_plural': 'Root categories',
            },
        ),
        migrations.AddField(
            model_name='categoryblog',
            name='root_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.rootcategoryblog', verbose_name='Root category'),
        ),
    ]