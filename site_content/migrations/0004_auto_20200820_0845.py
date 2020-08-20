# Generated by Django 2.2.10 on 2020-08-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0003_auto_20200816_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='concept_firstblock_background',
            field=models.ImageField(blank=True, null=True, upload_to='static', verbose_name='Première image background concept'),
        ),
        migrations.AlterField(
            model_name='content',
            name='concept_firstblock_content',
            field=models.TextField(default='default', verbose_name='Titre du second bloc concept'),
        ),
        migrations.AlterField(
            model_name='content',
            name='concept_firstblock_img',
            field=models.ImageField(blank=True, null=True, upload_to='static', verbose_name='Image premier bloc concept'),
        ),
        migrations.AlterField(
            model_name='content',
            name='concept_firstblock_title',
            field=models.CharField(default='default', max_length=200, verbose_name='Titre premier bloc concept'),
        ),
        migrations.AlterField(
            model_name='content',
            name='concept_secondblock_content',
            field=models.TextField(default='default', verbose_name='Contenu du second bloc concept'),
        ),
        migrations.AlterField(
            model_name='content',
            name='concept_secondblock_title',
            field=models.CharField(default='default', max_length=200, verbose_name='Titre du second bloc concept'),
        ),
        migrations.AlterField(
            model_name='content',
            name='concept_thirdblock_title',
            field=models.CharField(default='default', max_length=200, verbose_name='Titre du troisième bloc concept'),
        ),
        migrations.AlterField(
            model_name='content',
            name='homepage_content_img',
            field=models.ImageField(blank=True, null=True, upload_to='static', verbose_name="Image central page d'accueil"),
        ),
        migrations.AlterField(
            model_name='content',
            name='homepage_first_img',
            field=models.ImageField(blank=True, null=True, upload_to='static', verbose_name="Première image page d'accueil"),
        ),
    ]
