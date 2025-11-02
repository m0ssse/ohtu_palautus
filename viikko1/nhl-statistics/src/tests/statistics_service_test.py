import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_oikea_pelaaja_loytyy(self):
        pelaaja = self.stats.search("Lemieux")
        self.assertEqual(str(pelaaja), "Lemieux PIT 45 + 54 = 99")

    def test_olematon_pelaaja_ei_loydy(self):
        pelaaja = self.stats.search("Ransu")
        self.assertEqual(pelaaja, None)

    def test_joukkueen_kaikki_pelaajat(self):
        pelaajat = [str(pelaaja) for pelaaja in self.stats.team("EDM")]
        self.assertEqual(pelaajat, [
            "Semenko EDM 4 + 12 = 16",
            "Kurri EDM 37 + 53 = 90",
            "Gretzky EDM 3"
            "5 + 89 = 124"
        ])

    def test_top_palauttaa_oikean_maaran_pelaajia(self):
        for i in range(5):
            pelaajat = self.stats.top(i)
            self.assertEqual(len(pelaajat), i+1) #tehtäväpohjassa annettu metodi top palauttaa yhtä pidemmän listan kuin parametri, koska silmukan päättymisehtona on, että indeksi on yhtä suuri kuin parametri