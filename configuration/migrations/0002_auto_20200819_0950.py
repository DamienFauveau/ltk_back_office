# Generated by Django 2.2.10 on 2020-08-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name="Email utilisé pour l'envoi de mail"),
        ),
    ]