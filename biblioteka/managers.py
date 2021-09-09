from django.db import models

class KsiazkaQuerySet(models.QuerySet):
    def nowoczesne(self):
        return self.filter(rok_wydania__gte=2000)
    def stare(self):
        return self.filter(rok_wydania__lt=2000)

class KsiazkaManager(models.Manager):
    def get_queryset(self):
        return KsiazkaQuerySet(self.model, using=self._db)
    def nowoczesne(self):
        return self.get_queryset().nowoczesne()
    def stare(self):
        return self.get_queryset().stare()


# class KsiazkaNowoczesnaManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(rok_wydania__gte=2000)

# class KsiazkaStaraManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(rok_wydania__lt=2000)