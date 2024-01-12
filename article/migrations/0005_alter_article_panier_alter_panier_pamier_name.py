# Generated by Django 4.2.6 on 2024-01-11 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_panier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='panier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='article.panier'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='pamier_name',
            field=models.CharField(default='mon panier', max_length=128),
        ),
    ]
