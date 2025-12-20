import unittest
from tekoaly_parannettu import TekoalyParannettu


class TestTekoalyParannettu(unittest.TestCase):
    def setUp(self):
        self.tekoaly = TekoalyParannettu(10)

    def test_alustus(self):
        """Test that advanced AI initializes correctly"""
        self.assertEqual(len(self.tekoaly._muisti), 10)
        self.assertEqual(self.tekoaly._vapaa_muisti_indeksi, 0)
        self.assertTrue(all(x is None for x in self.tekoaly._muisti))

    def test_ensimmainen_siirto_kivi(self):
        """Test that first move is always rock"""
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, "k")

    def test_toinen_siirto_ilman_muistia_kivi(self):
        """Test that second move without memory is rock"""
        self.tekoaly.anna_siirto()
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, "k")

    def test_aseta_siirto_lisaa_muistiin(self):
        """Test that setting a move adds it to memory"""
        self.tekoaly.aseta_siirto("k")
        self.assertEqual(self.tekoaly._muisti[0], "k")
        self.assertEqual(self.tekoaly._vapaa_muisti_indeksi, 1)

    def test_muisti_tayttyy_oikein(self):
        """Test that memory fills up correctly"""
        for i, siirto in enumerate(["k", "p", "s", "k", "p"]):
            self.tekoaly.aseta_siirto(siirto)
            self.assertEqual(self.tekoaly._vapaa_muisti_indeksi, i + 1)

    def test_muisti_taynnä_vanhin_poistetaan(self):
        """Test that oldest move is removed when memory is full"""
        # Fill memory with 10 moves
        for i in range(10):
            self.tekoaly.aseta_siirto("k")
        
        self.assertEqual(self.tekoaly._vapaa_muisti_indeksi, 10)
        
        # Add one more - should remove oldest
        self.tekoaly.aseta_siirto("p")
        self.assertEqual(self.tekoaly._vapaa_muisti_indeksi, 10)
        self.assertEqual(self.tekoaly._muisti[9], "p")

    def test_oppii_kivi_vastaa_paperilla(self):
        """Test that AI learns to counter rock with paper"""
        # Player plays rock twice
        self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto("k")
        
        # Next time player plays rock, AI should predict rock and play paper
        self.tekoaly.aseta_siirto("k")
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, "p")

    def test_oppii_paperi_vastaa_saksilla(self):
        """Test that AI learns to counter paper with scissors"""
        # Player plays paper twice
        self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto("p")
        self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto("p")
        
        # Next time player plays paper, AI should predict paper and play scissors
        self.tekoaly.aseta_siirto("p")
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, "s")

    def test_oppii_sakset_vastaa_kivella(self):
        """Test that AI learns to counter scissors with rock"""
        # Player plays scissors twice
        self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto("s")
        self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto("s")
        
        # Next time player plays scissors, AI should predict scissors and play rock
        self.tekoaly.aseta_siirto("s")
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, "k")

    def test_erilaiset_muistikoot(self):
        """Test that different memory sizes work"""
        for koko in [3, 5, 20]:
            ai = TekoalyParannettu(koko)
            self.assertEqual(len(ai._muisti), koko)
            self.assertEqual(ai._vapaa_muisti_indeksi, 0)

    def test_tyhja_siirto_ei_tallenna(self):
        """Test that empty/None moves are not saved"""
        self.tekoaly.aseta_siirto(None)
        self.assertEqual(self.tekoaly._vapaa_muisti_indeksi, 0)
        
        self.tekoaly.aseta_siirto("")
        self.assertEqual(self.tekoaly._vapaa_muisti_indeksi, 0)


if __name__ == '__main__':
    unittest.main()
