# Generated by Django 4.2.6 on 2024-01-10 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_panier_articles_panier_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panier',
            old_name='products',
            new_name='article',
        ),
    ]
