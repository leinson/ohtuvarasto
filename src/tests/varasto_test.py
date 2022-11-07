import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_virhetilavuus_nollaantuu(self):
        self.varasto = Varasto(-10)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_virheellinen_alkusaldo_nollataan(self):
        self.varasto = Varasto(10, -5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_tayteen_ja_ylimaara_hukkaan(self):
        self.varasto = Varasto(10, 20)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_nega_maara(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertEqual(self.varasto.tilavuus, 10)
    
    def test_maara_suurempi_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(20)
        self.assertEqual(self.varasto.tilavuus, self.varasto.saldo)
    
    def test_nega_ottomaara(self):
        self.varasto.ota_varastosta(-10)
        self.assertEqual(self.varasto.tilavuus, 10)
    
    def test_maara_suurempi_kuin_saldo(self):
        self.varasto.ota_varastosta(10)
        self.assertEqual(self.varasto.saldo, 0)
    
    def test_tulostus_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10 BREAK")