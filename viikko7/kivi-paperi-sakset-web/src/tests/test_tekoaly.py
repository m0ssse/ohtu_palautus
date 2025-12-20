import unittest
from tekoaly import Tekoaly


class TestTekoaly(unittest.TestCase):
    def setUp(self):
        self.tekoaly = Tekoaly()

    def test_alustus(self):
        """Test that AI initializes with siirto at 0"""
        self.assertEqual(self.tekoaly._siirto, 0)

    def test_anna_siirto_kiertaa(self):
        """Test that AI cycles through p, s, k"""
        siirrot = []
        for i in range(6):
            siirrot.append(self.tekoaly.anna_siirto())
        
        # Should cycle: p, s, k, p, s, k (increments first, so 0→1→p, 1→2→s, 2→0→k)
        self.assertEqual(siirrot, ["p", "s", "k", "p", "s", "k"])

    def test_ensimmainen_siirto_paperi(self):
        """Test that first move is paper"""
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, "p")

    def test_toinen_siirto_sakset(self):
        """Test that second move is scissors"""
        self.tekoaly.anna_siirto()  # First move
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, "s")

    def test_kolmas_siirto_kivi(self):
        """Test that third move is rock"""
        self.tekoaly.anna_siirto()  # First move
        self.tekoaly.anna_siirto()  # Second move
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, "k")

    def test_aseta_siirto_ei_tee_mitaan(self):
        """Test that aseta_siirto does nothing (as intended)"""
        self.tekoaly.anna_siirto()
        before = self.tekoaly._siirto
        self.tekoaly.aseta_siirto("k")
        after = self.tekoaly._siirto
        self.assertEqual(before, after)

    def test_siirto_counter_kasvaa(self):
        """Test that internal counter increments"""
        self.assertEqual(self.tekoaly._siirto, 0)
        self.tekoaly.anna_siirto()
        self.assertEqual(self.tekoaly._siirto, 1)
        self.tekoaly.anna_siirto()
        self.assertEqual(self.tekoaly._siirto, 2)


if __name__ == '__main__':
    unittest.main()
