from biblioteka.models import Autor
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

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