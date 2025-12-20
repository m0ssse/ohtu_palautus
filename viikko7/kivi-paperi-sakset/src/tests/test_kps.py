import unittest
from kps import KiviPaperiSakset, KPSPelaajaVsPelaaja, KPSTekoaly, luo_peli
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class TestKiviPaperiSakset(unittest.TestCase):
    
    def test_onko_ok_siirto_hyvaksyy_kiven(self):
        """Test that 'k' is accepted as valid move"""
        peli = KPSPelaajaVsPelaaja()
        self.assertTrue(peli._onko_ok_siirto("k"))

    def test_onko_ok_siirto_hyvaksyy_paperin(self):
        """Test that 'p' is accepted as valid move"""
        peli = KPSPelaajaVsPelaaja()
        self.assertTrue(peli._onko_ok_siirto("p"))

    def test_onko_ok_siirto_hyvaksyy_sakset(self):
        """Test that 's' is accepted as valid move"""
        peli = KPSPelaajaVsPelaaja()
        self.assertTrue(peli._onko_ok_siirto("s"))

    def test_onko_ok_siirto_hylkaa_virheelliset(self):
        """Test that invalid moves are rejected"""
        peli = KPSPelaajaVsPelaaja()
        self.assertFalse(peli._onko_ok_siirto("x"))
        self.assertFalse(peli._onko_ok_siirto(""))
        self.assertFalse(peli._onko_ok_siirto("kivi"))
        self.assertFalse(peli._onko_ok_siirto("1"))


class TestKPSPelaajaVsPelaaja(unittest.TestCase):
    
    def test_luonti(self):
        """Test that player vs player game can be created"""
        peli = KPSPelaajaVsPelaaja()
        self.assertIsNotNone(peli)


class TestKPSTekoaly(unittest.TestCase):
    
    def test_luonti_perus_tekoalyllä(self):
        """Test that AI game can be created with basic AI"""
        tekoaly = Tekoaly()
        peli = KPSTekoaly(tekoaly)
        self.assertIsNotNone(peli)
        self.assertEqual(peli.tekoaly, tekoaly)

    def test_luonti_parannetulla_tekoalyllä(self):
        """Test that AI game can be created with advanced AI"""
        tekoaly = TekoalyParannettu(10)
        peli = KPSTekoaly(tekoaly)
        self.assertIsNotNone(peli)
        self.assertEqual(peli.tekoaly, tekoaly)

    def test_toisen_siirto_palauttaa_tekoalyn_siirron(self):
        """Test that _toisen_siirto returns AI move"""
        tekoaly = Tekoaly()
        peli = KPSTekoaly(tekoaly)
        
        # First move should be paper (AI increments 0→1 first)
        siirto = peli._toisen_siirto("k")
        self.assertEqual(siirto, "p")


class TestLuoPeli(unittest.TestCase):
    
    def test_luo_pelaaja_vs_pelaaja(self):
        """Test creating player vs player game"""
        peli = luo_peli("a")
        self.assertIsInstance(peli, KPSPelaajaVsPelaaja)

    def test_luo_tekoaly_peli(self):
        """Test creating AI game"""
        peli = luo_peli("b")
        self.assertIsInstance(peli, KPSTekoaly)
        self.assertIsInstance(peli.tekoaly, Tekoaly)

    def test_luo_parannettu_tekoaly_peli(self):
        """Test creating advanced AI game"""
        peli = luo_peli("c")
        self.assertIsInstance(peli, KPSTekoaly)
        self.assertIsInstance(peli.tekoaly, TekoalyParannettu)


if __name__ == '__main__':
    unittest.main()
