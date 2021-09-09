from biblioteka.models import Autor
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save, pre_save
from django.core.signals import request_finished

nasz_signal = Signal(providing_args=['imie'])

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
    try:
        print(Autor.objects.get(id=instance.id).imie)
    except Autor.DoesNotExist:
        print('Nowy aktor')

@receiver(request_finished)
def strona_wczytana(sender, **kwargs):
    print('Strona sie wczytala')

@receiver(nasz_signal)
def podane_imie(sender, **kwargs):
    print('Podane imie: ', kwargs.get('imie'))
