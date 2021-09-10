from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import nowy_form

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