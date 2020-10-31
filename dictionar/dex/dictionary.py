""" Modulul responsabil pentru obtinerea definitiei de pe dex.ro. """
import requests
from bs4 import BeautifulSoup as soup


def generate_link(cuvant):
    """ Functia genereaza linkul potrivit pentru cuvantul dat. 
        Date de intrare: cuvantul ca string.
        Date de iesire: url-ul la care este gasita definitia ca string. """
    #url = 'https://www.dictionarroman.ro/?c={}'.format(cuvant)
    url = 'https://dexonline.ro/definitie/{}'.format(cuvant)
    return url


def fetch_page_html(url):
    """ Functia obtine html-ul paginii aflate la url-ul dat.
        Date de intrare: url ca string.
        Date de iesire: html-ul paginii ca string. """
    r = requests.get(url)
    page = r.text
    r.close()
    return page


def return_def(page):
    """ Extrage doar textul primei definitii din tot fisierul html.
        Date de intrare: pagina html ca string.
        Date de iesire: definitia cuvantului dat. 
                        Ridica ValueError daca nu este gasita definitia. """
    page_soup = soup(page, 'html.parser')
    definitie = page_soup.find('span', {'class':'def'})
    if definitie is None:
        raise ValueError
    return definitie.get_text()


def fetch_definition(cuvant):
    """ Functia ofera definitia cuvantului dat.
        Date de intrare: cuvantul ca string.
        Date de iesire: definitia cuvantului ca string. """
    link = generate_link(cuvant)
    pagina = fetch_page_html(link)
    try:
        definitie = return_def(pagina)
        definitie = pregatire_definitie(definitie)
    except ValueError:
        definitie = None
    return definitie


def pregatire_definitie(definitie):
    """ Functia pregateste definitia petru a fi introdusa in baza de date.
        Date de intrare: Definitia ca string
        Date de iesire: Definitia ca string conform bazei de date. """
    if len(definitie) > 5000:
        definitie = definitie[:5000]
    return definitie


def test_pregatire_definitie():
    """ Functia de test pentru pregatire_definitie. """
    definitie = ["a" for i in range(6000)]
    assert len(pregatire_definitie(definitie)) == 5000
