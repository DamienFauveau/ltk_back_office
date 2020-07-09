# Generated by Django 2.2.10 on 2020-07-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Durée en mois')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Taux')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Taux',
                'verbose_name_plural': 'Taux',
            },
        ),
    ]
