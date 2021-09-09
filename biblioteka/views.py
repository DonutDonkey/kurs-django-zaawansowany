from biblioteka.models import Autor
from django.shortcuts import render
from django.http import HttpResponse
from .signals import nasz_signal
# Create your views here.
def glowny(request):
    nasz_signal.send(sender=Autor, imie='Admin')
    return HttpResponse('to jest nasza glowna strona')