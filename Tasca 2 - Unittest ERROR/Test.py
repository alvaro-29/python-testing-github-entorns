# Test Prova_escrita_03 i Prova_escrita_04 - Fet per Álvaro Gómez Fernández

# Importem unittest:
import unittest

# Importem tot dels fitxers dels testos 3 i 4:
from Prova_escrita_03 import *
from Prova_escrita_04 import *

class TestProvaEscrita03(unittest.TestCase):
    """
    Classe de tests per a Prova_escrita_03.
    Conté proves unitàries per a les funcions definides al fitxer Prova_escrita_03.
    """

    def test_trobar_millor_pitjor_rendiment(self):
        """Test per validar la funció trobar_millor_pitjor_rendiment."""
        millor, pitjor = trobar_millor_pitjor_rendiment(m1, m2, m3)
        self.assertEqual(millor, 10.5)  # Comprova que el millor rendiment sigui correcte.
        self.assertEqual(pitjor, 15.0)  # Comprova que el pitjor rendiment sigui correcte.
        
        millor, pitjor = trobar_millor_pitjor_rendiment()
        self.assertEqual(millor, 0)  # Comprova el cas buit.
        self.assertEqual(pitjor, 0)

    def test_comptar_estudiants(self):
        """Test per validar la funció comptar_estudiants."""
        resultat = comptar_estudiants(notes_estudiants)
        self.assertEqual(resultat, 4)  # Comprova que hi ha 4 estudiants.

    def test_comptar_estudiants_materia(self):
        """Test per validar la funció comptar_estudiants_matèria."""
        resultat = comptar_estudiants_matèria(notes_estudiants, "Matemàtiques")
        self.assertEqual(resultat, 3)  # Comprova que 2 estudiants cursen Matemàtiques.
        
        resultat = comptar_estudiants_matèria(notes_estudiants, "Física")
        self.assertEqual(resultat, 0)  # Comprova que cap estudiant cursa Física.

class TestProvaEscrita04(unittest.TestCase):
    """
    Classe de tests per a Prova_escrita_04.
    Conté proves unitàries per a les funcions definides al fitxer Prova_escrita_04.
    """

    def test_cercar_element(self):
        """Test per validar la funció cercar_el."""
        trobat, posicio = cercar_el(m_ex, 5, True)
        self.assertTrue(trobat)  # Comprova que l'element existeix.
        self.assertEqual(posicio, (1, 1))  # Comprova la posició correcta.

        trobat, posicio = cercar_el(m_ex, 10, True)
        self.assertFalse(trobat)  # Comprova que l'element no existeix.
        self.assertIsNone(posicio)  # Comprova que no hi ha posició.

    def test_sumar_fila(self):
        """Test per validar la funció sumar_fila."""
        resultat = sumar_fila(m_ex, 0)
        self.assertEqual(resultat, 6)  # Comprova la suma de la primera fila.

        resultat = sumar_fila(m_ex, 10)
        self.assertEqual(resultat, 0)  # Comprova un índex invàlid.

    def test_sumar_matriu(self):
        """Test per validar la funció sumar_matriu."""
        resultat = sumar_matriu(m_ex)
        self.assertEqual(resultat, 45)  # Comprova la suma total de la matriu.

    def test_transformar(self):
        """Test per validar la funció transformar."""
        transformar(m_ex, 10, "-")
        self.assertEqual(m_ex, [[11, 12, 13], [14, 15, 16], [17, 18, 19]])  # Comprova la transformació suma.

        transformar(m_ex, 1, "-")
        self.assertEqual(m_ex, [[10, 11, 12], [13, 14, 15], [16, 17, 18]])  # Comprova la transformació resta.

# Per executar els tests utilitzarem el __name__ amb unittest:
if __name__ == "__main__":
    unittest.main()

# Fet per Álvaro Gómez Fernández