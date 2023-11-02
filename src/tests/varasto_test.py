import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        # testaa kaikki virhetilanteet varastloluokkaa luodessa
        self.varasto = Varasto(-10, -20)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

        self.varasto = Varasto(10, 20)

        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

        # palauta varaston saldo alkperäiseen
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

    def test_virheellisen_maaran_lisays(self):
        vanha_saldo = self.varasto.paljonko_mahtuu()

        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), vanha_saldo)

    def test_tilavuuden_ylivuoto(self):
        self.varasto.lisaa_varastoon(999)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_virheellisen_maaran_poisto(self):
        vanha_saldo = self.varasto.paljonko_mahtuu()

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 999)

    def test_ylisuuri_poisto(self):
        self.varasto.ota_varastosta(999)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), self.varasto.tilavuus)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijonotulostus(self):
        self.varasto.ota_varastosta(999)

        oletettu_tila = self.varasto.paljonko_mahtuu()

        self.assertEqual(str(self.varasto), f"saldo = 0.0, vielä tilaa {oletettu_tila}")