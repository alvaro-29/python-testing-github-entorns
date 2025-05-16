# Pytest - Fet per Álvaro Gómez Fernández

# Importació de les funcions a provar i el mòdul pytest:
from prova_escrita_5 import *
import pytest


# Test per verificar la funcionalitat de la funció "llibres_per_categoria":
@pytest.mark.parametrize("biblioteca, categoria, res_esperat",[(biblioteca, "fantasia", ['El Senyor dels Anells']),(biblioteca, "ciència-ficció", ['1984'])])
def test_1(biblioteca, categoria, res_esperat):
    """
    Test per comprovar que la funció retorna correctament els llibres d'una categoria determinada.
    :param biblioteca: Diccionari que representa la biblioteca.
    :param categoria: Categoria dels llibres a buscar.
    :param res_esperat: Llista amb els llibres esperats.
    """
    resultat = llibres_per_categoria(biblioteca, categoria)
    assert resultat == res_esperat

# Test per verificar si un llibre està disponible a la biblioteca:
@pytest.mark.parametrize("biblioteca, llibre, res_esperat",[(biblioteca, "Crim i Càstig", True),(biblioteca, "El Quixot", False)])
def test_2(biblioteca, llibre, res_esperat):
    """
    Test per comprovar si un llibre està disponible a la biblioteca.
    :param biblioteca: Diccionari que representa la biblioteca.
    :param llibre: Nom del llibre a comprovar.
    :param res_esperat: Booleà que indica si el llibre està disponible o no.
    """
    resultat = esta_disponible(biblioteca, llibre)
    assert resultat == res_esperat

# Test per verificar si un usuari té préstecs actius:
@pytest.mark.parametrize("biblioteca, usuari, res_esperat",[(biblioteca, "Joan", False),(biblioteca, "Maria", True)])
def test_3(biblioteca, usuari, res_esperat):
    """
    Test per comprovar si un usuari té préstecs actius a la biblioteca.
    :param biblioteca: Diccionari que representa la biblioteca.
    :param usuari: Nom de l'usuari a comprovar.
    :param res_esperat: Booleà que indica si l'usuari té préstecs actius.
    """
    resultat = usuari_te_prestecs(biblioteca, usuari)
    assert resultat == res_esperat

# Test per verificar el total de dies que un llibre ha estat prestat:
@pytest.mark.parametrize("biblioteca, llibre, res_esperat",[(biblioteca, "El Quixot", 47),(biblioteca, "1984", 53)])
def test_4(biblioteca, llibre, res_esperat):
    """
    Test per comprovar el total de dies que un llibre ha estat prestat.
    :param biblioteca: Diccionari que representa la biblioteca.
    :param llibre: Nom del llibre a comprovar.
    :param res_esperat: Enter que indica el total de dies esperats.
    """
    resultat = dies_prestec_total(biblioteca, llibre)
    assert resultat == res_esperat

# Fet per Álvaro Gómez Fernández