# Generated by Django 2.2.10 on 2020-05-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0002_artwork_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='price',
            field=models.DecimalField(decimal_places=2, default=156, max_digits=7, verbose_name='Prix (€)'),
            preserve_default=False,
        ),
    ]