from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey( # ForeignKey - odkazuje na jinou tabulku, autoří jsou v jiné tabulce
        "auth.User",
        on_delete=models.CASCADE) # když smažu uživatele, smažou se i jeho příspěvky
    title = models.CharField(max_length=200) # CharField = textové políčko, kratší text
    text = models.TextField() # TextField = delší text
    created_date = models.DateTimeField(
            default=timezone.now) # vrací aktuální datum a čas
    published_date = models.DateTimeField(
            blank=True, null=True) # políčko může být prázdné

    def publish(self): # metody mají první atribut self, protože berou ten objekt, ve kterém jsou
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # metoda, jak se bude příspěvek převádět na řetězec
        return self.title # dostaneme titulek
