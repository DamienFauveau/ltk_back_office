# Generated by Django 2.2.10 on 2020-07-07 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_auto_20200605_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rate',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
