from django.core import validators
from django.db import models
from biblioteka.managers import KsiazkaManager
from django.core.validators import MaxValueValidator
from .validators import validate_rok

class Autor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.imie + " " + self.nazwisko

# post_save.connect(autor_po_zapisaniu, sender=Autor)

class Gatunek():
    NIEZNANY = 0
    FANTASY = 1
    HORROR = 2
    DRAMA = 3
    GATUNKI = (
        (NIEZNANY, 'Nieznany'),
        (FANTASY, 'Fantasy'),
        (HORROR, 'Horror'),
        (DRAMA, 'Drama'),
    )
        
class Ksiazka(models.Model):
    tytul = models.CharField(max_length=50, blank=False)
    rok_wydania = models.IntegerField(blank=False, validators=[MaxValueValidator(2020)])
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='ksiazki')
    gatunek = models.PositiveSmallIntegerField(choices=Gatunek.GATUNKI, default=0)

    objects = models.Manager() # jesli customowy manager jest to defaultowy objects przestaje istniec wiec dodajemy
    ksiazki = KsiazkaManager()

# Validator wyrzuci w interfejswie admina itp ale nie w konsoli
    def save(self, *args, **kwargs):
        # if self.rok_wydania > 2020:
        #     raise ValueError('Rok wydania wiekszy niz 2020')
        # super(Ksiazka, self).save(*args, **kwargs)
        validate_rok(self.rok_wydania)

    def __str__(self):
        return self.tytul

    def jest_nowoczesna(self) -> bool:
        return self.rok_wydania > 2000

    class Meta:
        # db_table = 'ksiazki' #inna nazwa przechowyzania ksiazki
        # ordering = ['rok_wydania'] # orderowanie w bazie, - dla malejacych
        # order_with_respect_to = 'autor'  #sortowanie wzgledem czegos
        verbose_name = 'książka' #nazwa w bazie
        verbose_name_plural = 'książki' #nazwa w liczbie mnogiej
        #kombinacja tych wartosci musi byc unikalna
        unique_together = ['tytul', 'rok_wydania']
        #indexowanie, przyspieszanie iteracji po databasie
        indexes = [
            models.Index(fields=['tytul'], name=['tytul_indx']),
            models.Index(fields=['tytul', 'rok_wydania'])
        ]
        # permissions = [
        #     ('can_update_ksiazka', "Może zmieniać książke")
        # ]