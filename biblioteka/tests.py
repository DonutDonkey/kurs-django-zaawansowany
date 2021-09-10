from biblioteka.validators import validate_rok
from biblioteka.models import Autor, Ksiazka
from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import nowy_form
from django.core.exceptions import ValidationError
from .forms import NaszForm

# Create your tests here.
class BibliotekaTests(TestCase):

    def test_nasz_pierwszy(self):
        assert 1 == 1

#URL test
    def test_url_nowy_form(self):
        url = reverse('nowy_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func, nowy_form)
        
#VIEW test
    def test_view_nowy(self):
        client = Client()
        response = client.get(reverse('nowy_form'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'nasz_form.html')

#MODELS test
    def setUp(self) -> None:
        self.autor = Autor.objects.create(imie='Testowy', nazwisko='Autor')
        self.ksiazka = Ksiazka.objects.create(tytul='testowa', rok_wydania=2019, autor=self.autor)

    def test_autor_str(self):
        self.assertEquals(str(self.autor), 'Testowy Autor')
    
    def test_autor_str2(self):
        autor = Autor.objects.first()
        self.assertEquals(str(self.autor), 'Testowy Autor')

    def test_ksiazka_not_empty(self) -> None:
        ksiazka = Ksiazka.objects.create(tytul='testowa', rok_wydania=2010, autor=self.autor)
        self.assertNotEqual(ksiazka, None)

    def test_ksiazka_is_unique(self) -> None:
        with self.assertRaises(Exception):
            Ksiazka.objects.create(tytul='testowa', rok_wydania=2019, autor=self.autor)
#Manager test
    def test_ksiazki_manager(self) -> None:
        ksiazki = Ksiazka.ksiazki.nowoczesne()
        self.assertGreater(len(ksiazki),0)

#Functions test
    def test_funkcja_validate_rok(self):
        self.assertRaises(ValidationError, validate_rok, 2025)

    def test_funkcja_validate_rok(self):
        self.assertEqual(validate_rok(2019), 2019)

#FORMS test
    def test_nasz_from_valid(self):
        form = NaszForm(data={
            'imie': 'Test',
            'rok': 2020
        })
        self.assertTrue(form.is_valid())

    def test_nasz_from_valid(self):
        form = NaszForm(data={
            'imie': 'Test',
            'rok': 2025
        })
        self.assertFalse(form.is_valid())