# Generated by Django 2.2.10 on 2020-08-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20200816_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='photo',
            field=models.ImageField(default='/default.jpg', upload_to='artworks'),
        ),
    ]
