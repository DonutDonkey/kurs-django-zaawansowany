from django.apps import AppConfig


class BibliotekaConfig(AppConfig):
    name = 'biblioteka'

    def ready(self):
        import biblioteka.signals
