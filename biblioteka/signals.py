import logging
from biblioteka.models import Autor
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save, pre_save
from django.core.signals import request_finished

nasz_signal = Signal(providing_args=['imie'])

autor_log = logging.getLogger('autor_log')
autor_log.setLevel(logging.DEBUG)

log_handler = logging.FileHandler('logs/autor.log')
log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
autor_log.addHandler(log_handler)

# sender : co wywoławo funkcje
# instance : obiekt który wywołał funkcje
# **kwargs : argumenty w funkcji
@receiver([post_save], sender=Autor)
def autor_po_zapisaniu(sender, instance, **kwargs):
    print('Autor saved')
    print(instance.imie)
    autor_log.info('Autor zapisane przez : ' + instance.imie + ' ' + instance.nazwisko)

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
