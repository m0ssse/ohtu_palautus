import unittest
from tuomari import Tuomari


class TestTuomari(unittest.TestCase):
    def setUp(self):
        self.tuomari = Tuomari()

    def test_alustus(self):
        """Test that Tuomari initializes with zero scores"""
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)
        self.assertEqual(self.tuomari.tasapelit, 0)

    def test_tasapeli(self):
        """Test that ties are recorded correctly"""
        self.tuomari.kirjaa_siirto("k", "k")
        self.assertEqual(self.tuomari.tasapelit, 1)
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)

    def test_kaikki_tasapelit(self):
        """Test all tie combinations"""
        self.tuomari.kirjaa_siirto("k", "k")
        self.tuomari.kirjaa_siirto("p", "p")
        self.tuomari.kirjaa_siirto("s", "s")
        self.assertEqual(self.tuomari.tasapelit, 3)

    def test_eka_voittaa_kivi_voittaa_sakset(self):
        """Test that rock beats scissors"""
        self.tuomari.kirjaa_siirto("k", "s")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)

    def test_eka_voittaa_sakset_voittaa_paperi(self):
        """Test that scissors beat paper"""
        self.tuomari.kirjaa_siirto("s", "p")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)

    def test_eka_voittaa_paperi_voittaa_kivi(self):
        """Test that paper beats rock"""
        self.tuomari.kirjaa_siirto("p", "k")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)

    def test_toka_voittaa_kivi_voittaa_sakset(self):
        """Test that second player wins with rock vs scissors"""
        self.tuomari.kirjaa_siirto("s", "k")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 1)

    def test_toka_voittaa_sakset_voittaa_paperi(self):
        """Test that second player wins with scissors vs paper"""
        self.tuomari.kirjaa_siirto("p", "s")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 1)

    def test_toka_voittaa_paperi_voittaa_kivi(self):
        """Test that second player wins with paper vs rock"""
        self.tuomari.kirjaa_siirto("k", "p")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 1)

    def test_useita_kierroksia(self):
        """Test multiple rounds with mixed results"""
        self.tuomari.kirjaa_siirto("k", "s")  # Eka voittaa
        self.tuomari.kirjaa_siirto("p", "p")  # Tasapeli
        self.tuomari.kirjaa_siirto("s", "k")  # Toka voittaa
        self.tuomari.kirjaa_siirto("k", "p")  # Toka voittaa
        
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 2)
        self.assertEqual(self.tuomari.tasapelit, 1)

    def test_str_metodi(self):
        """Test string representation"""
        self.tuomari.kirjaa_siirto("k", "s")
        self.tuomari.kirjaa_siirto("p", "p")
        
        tuloste = str(self.tuomari)
        self.assertIn("1 - 0", tuloste)
        self.assertIn("Tasapelit: 1", tuloste)

    def test_peli_ei_paattynyt_alussa(self):
        """Test that game is not ended at start"""
        self.assertFalse(self.tuomari.peli_paattynyt())

    def test_peli_paattynyt_kun_eka_voittaa_kolme(self):
        """Test that game ends when first player reaches 3 wins"""
        for i in range(3):
            self.tuomari.kirjaa_siirto("k", "s")
        self.assertTrue(self.tuomari.peli_paattynyt())

    def test_peli_paattynyt_kun_toka_voittaa_kolme(self):
        """Test that game ends when second player reaches 3 wins"""
        for i in range(3):
            self.tuomari.kirjaa_siirto("s", "k")
        self.assertTrue(self.tuomari.peli_paattynyt())

    def test_peli_ei_paattynyt_alle_kolme(self):
        """Test that game doesn't end before 3 wins"""
        for i in range(2):
            self.tuomari.kirjaa_siirto("k", "s")
        self.assertFalse(self.tuomari.peli_paattynyt())

    def test_peli_paattynyt_yli_kolme_voittoa(self):
        """Test that game is still ended with more than 3 wins"""
        for i in range(5):
            self.tuomari.kirjaa_siirto("k", "s")
        self.assertTrue(self.tuomari.peli_paattynyt())

    def test_peli_paattynyt_tasatilanteessa_kolme_kolme(self):
        """Test that game ends when both players reach 3 wins"""
        # Play 3 wins for each player
        for i in range(3):
            self.tuomari.kirjaa_siirto("k", "s")  # Eka wins
            self.tuomari.kirjaa_siirto("s", "k")  # Toka wins
        
        self.assertEqual(self.tuomari.ekan_pisteet, 3)
        self.assertEqual(self.tuomari.tokan_pisteet, 3)
        self.assertTrue(self.tuomari.peli_paattynyt())

    def test_peli_paattynyt_tarkalleen_kolmella_voitolla(self):
        """Test that game ends exactly at 3 wins"""
        # 2 wins - game should not be ended
        for i in range(2):
            self.tuomari.kirjaa_siirto("k", "s")
        self.assertFalse(self.tuomari.peli_paattynyt())
        
        # 3rd win - game should end
        self.tuomari.kirjaa_siirto("k", "s")
        self.assertTrue(self.tuomari.peli_paattynyt())

    def test_peli_jatkuu_tasapelien_kanssa(self):
        """Test that game continues with ties and doesn't count towards 3 wins"""
        # 2 wins and 10 ties
        for i in range(2):
            self.tuomari.kirjaa_siirto("k", "s")  # Eka wins
        for i in range(10):
            self.tuomari.kirjaa_siirto("k", "k")  # Ties
        
        self.assertEqual(self.tuomari.ekan_pisteet, 2)
        self.assertEqual(self.tuomari.tasapelit, 10)
        self.assertFalse(self.tuomari.peli_paattynyt())


if __name__ == '__main__':
    unittest.main()
