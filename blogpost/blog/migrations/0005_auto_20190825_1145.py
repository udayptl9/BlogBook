# Generated by Django 2.2.3 on 2019-08-25 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_posts_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='file',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
    ]
