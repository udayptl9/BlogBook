# Generated by Django 2.2.3 on 2019-08-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190814_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
    ]