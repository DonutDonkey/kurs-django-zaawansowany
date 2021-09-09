from biblioteka.models import Autor, Ksiazka
from django.shortcuts import render
from django.http import HttpResponse
from .signals import nasz_signal
from django.db import transaction
from django.core.mail import send_mail

# Create your views here.
def glowny(request):
    nasz_signal.send(sender=Autor, imie='Admin')
    autor = {'imie': 'Walter', 'nazwisko': 'White'}
    ksiazka = {'tytul': 'Niebieskie cuda', 'rok_wydania': 2017}
    dodaj_do_bazy(autor, ksiazka)
    return HttpResponse('to jest nasza glowna strona')

def wysylanie_maila():
    send_mail(
        subject='temat',
        message='link klikniety',
        from_email='test@test.net',
        recipient_list=['abc@abc.com'],
        fail_silently=False
    )
#transaction atomic stworz wszystko albo nic
@transaction.atomic()
def dodaj_do_bazy(autor, ksiazka):
    with transaction.atomic():
        n_autor = Autor.objects.create(**autor)
        n_ksiazka = Ksiazka(**ksiazka)
        n_ksiazka.autor = n_autor
        n_ksiazka.save()