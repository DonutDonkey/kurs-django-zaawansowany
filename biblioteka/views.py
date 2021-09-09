from biblioteka.models import Autor, Ksiazka
from django.shortcuts import render
from django.http import HttpResponse, request
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

def wysylanie_maila(request):
    # send_mail(
    #     subject='temat',
    #     message='link klikniety',
    #     from_email='test@test.net',
    #     recipient_list=['abc@abc.com'],
    #     fail_silently=False
    # )

    if request.method == 'POST':
        if request.POST.get('email', False):
            email = request.POST['email']
            wiadomosc = 'form message' + email
            send_mail(
                subject='temat',
                message=wiadomosc,
                from_email=email,
                recipient_list=['abc@abc.com'],
                fail_silently=False
            )
            return HttpResponse('Mail zostal wyslany')
               
    return render(request, 'email_form.html')

    # return HttpResponse('to wysle naszego maila')

#transaction atomic stworz wszystko albo nic
@transaction.atomic()
def dodaj_do_bazy(autor, ksiazka):
    with transaction.atomic():
        n_autor = Autor.objects.create(**autor)
        n_ksiazka = Ksiazka(**ksiazka)
        n_ksiazka.autor = n_autor
        n_ksiazka.save()