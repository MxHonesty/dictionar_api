""" Modul responsabil pentru definirea modelelor abstracte din baza de date. """
from django.db import models


class Cuvant(models.Model):
    """ Modelul din baza de date pentru un cuvant. 
        Clasa are membrii: cuvant_text(string) - textul cuvantului.
                           cautari(int) - numarul de accesari al cuvantului."""
    cuvant_text = models.CharField(max_length=100)
    cautari = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cuvant_text
        

class Definitie(models.Model):
    """ Modelul din baza de date pentru o definitie. 
        Clasa are membrii: defnitie_text(string) - definitia stocata.
                           cuvant(cheie straina) - cuvantul. """
    definitie_text = models.CharField(max_length = 5000)
    cuvant = models.ForeignKey(Cuvant, on_delete=models.CASCADE)

    def __str__(self):
        return self.definitie_text
