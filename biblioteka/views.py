from django.shortcuts import render
from django.http import HttpResponse
# from .signals import nasz_sygnal
from .models import Ksiazka, Autor
from django.db import transaction
from django.core.mail import send_mail

def glowna(request):
    # nasz_sygnal.send(sender=Autor, imie="Krystian")
    autor = {'imie': "Walter", 'nazwisko': 'White'}
    ksiazka = {'tytul': "Niebieskie cuda", 'rok_wydanie': 2017}
    dodaj_do_bazy(autor, ksiazka)
    return HttpResponse("To jest nasza glowna strona")

def wyslanie_maila(request):
    if request.method == 'POST':
        if request.POST.get('email', False):
            email = request.POST['email']
            wiadomosc = "Naprawde klikneli na link: " + email
            ksiazki = Ksiazka.objects.all()
            for ksiazka in ksiazki:
                wiadomosc += '\n\r' + ksiazka.tytul
            send_mail(
                "Odwiedzili nasza strone!",
                wiadomosc,
                email,
                ['hiketi5027@hideemail.net'],
                fail_silently=False
            )
            return HttpResponse("Mail zostal wyslany")

    return render(request, 'email_form.html')



def dodaj_do_bazy(autor, ksiazka):

    with transaction.atomic():
        nowy_autor = Autor.objects.create(**autor)
        nowa_ksiazka = Ksiazka(**ksiazka)
        nowa_ksiazka.autor = nowy_autor
        nowa_ksiazka.save()