# Generated by Django 4.2.6 on 2024-01-11 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='panier',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.panier'),
        ),
    ]