# Generated by Django 2.2.10 on 2020-06-28 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='UserProfile',
            new_name='user',
        ),
    ]