# Generated by Django 2.2.10 on 2020-08-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200811_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.CharField(blank=True, default='default company', max_length=256, null=True, verbose_name='Entreprise'),
        ),
    ]
