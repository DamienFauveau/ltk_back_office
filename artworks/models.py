from django.db import models

from artists.models import Artist

class Artwork(models.Model):

    name = models.CharField(
        verbose_name="Nom",
        max_length=200,
        blank=False,
        null=False,
    )

    height = models.DecimalField(
        verbose_name="Hauteur (cm)",
        max_digits=4, 
        decimal_places=1,
        blank=False,
        null=False,
    )

    width = models.DecimalField(
        verbose_name="Largeur (cm)",
        max_digits=4, 
        decimal_places=1,
        blank=False,
        null=False,
    )

    price = models.DecimalField(
        verbose_name="Prix (€)",
        max_digits=7, 
        decimal_places=0,
        blank=False,
        null=False,
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name = "Artiste",
        db_index=True,
        null=False,
        blank=False,
    )

    style = models.ForeignKey(
        "Artwork_Style",        
        on_delete=models.CASCADE,
        verbose_name = "Style",
        db_index=True,
        null=False,
        blank=False,
        default='',
    )

    category = models.ForeignKey(
        "Artwork_Category",        
        on_delete=models.CASCADE,
        verbose_name = "Catégorie",
        db_index=True,
        null=False,
        blank=False,
        default='',
    )

    photo = models.ImageField(upload_to='artworks', default='/default.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Oeuvre"
        verbose_name_plural = "Oeuvres"

class Artwork_Style(models.Model):

    name = models.CharField(
        verbose_name="Nom",
        max_length=200,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Style de l'oeuvre"
        verbose_name_plural = "Style des oeuvres"

class Artwork_Category(models.Model):

    name = models.CharField(
        verbose_name="Nom",
        max_length=200,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catégorie de l'oeuvre"
        verbose_name_plural = "Catégories des oeuvres"