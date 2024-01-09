# Generated by Django 4.2.6 on 2024-01-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='uploader',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]