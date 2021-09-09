from django.db import models
from biblioteka.managers import KsiazkaManager
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class Autor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=20, blank=False)
    data_urodzenia = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.imie + " " + self.nazwisko
# sender : co wywoławo funkcje
# instance : obiekt który wywołał funkcje
# **kwargs : argumenty w funkcji
@receiver([post_save], sender=Autor)
def autor_po_zapisaniu(sender, instance, **kwargs):
    print('Autor saved')
    print(instance.imie)
@receiver([pre_save], sender=Autor)
def autor_po_zapisaniu(sender, instance, **kwargs):
    print('Autor before being saved')

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
    rok_wydania = models.IntegerField(blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='ksiazki')
    gatunek = models.PositiveSmallIntegerField(choices=Gatunek.GATUNKI, default=0)

    objects = models.Manager() # jesli customowy manager jest to defaultowy objects przestaje istniec wiec dodajemy
    ksiazki = KsiazkaManager()

    def __str__(self):
        return self.tytul

    class Meta:
        # db_table = 'ksiazki' #inna nazwa przechowyzania ksiazki
        # ordering = ['rok_wydania'] # orderowanie w bazie, - dla malejacych
        # order_with_respect_to = 'autor'  #sortowanie wzgledem czegos
        verbose_name = 'książka' #nazwa w bazie
        verbose_name_plural = 'książki' #nazwa w liczbie mnogiej
        #kombinacja tych wartosci musi byc unikalna
        unique_together = ['tytul', 'rok_wydania']
        #indexowanie, przyspieszanie iteracji po databasie
        # indexes = [
        #     models.Index(fields=['tytul'], name=['tytul_indx']),
        #     models.Index(fields=['tytul', 'rok_wydania'])
        # ]
        permissions = [
            ('can_update_ksiazka', "Może zmieniać książke")
        ]