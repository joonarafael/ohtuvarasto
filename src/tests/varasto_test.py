"""Module to perform the Varasto tests.
"""

import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    """Class object to handle the testing.

    Args:
        unittest: performing unittest
    """
    def setUp(self):
        """Check the initialization process.
        """
        self.varasto = Varasto(-10, -20)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

        self.varasto = Varasto(10, 20)

        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Empty storage.
        """
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Nonempty storage.
        """
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Simple balance addition.
        """
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Available space calculated correctly?
        """
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Storage capacity substraction.
        """
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Available capacity increases after balance withdrawal.
        """
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellisen_maaran_lisays(self):
        """Illegal argument for addition.
        """
        vanha_saldo = self.varasto.paljonko_mahtuu()

        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), vanha_saldo)

    def test_tilavuuden_ylivuoto(self):
        """Overflow of addition.
        """
        self.varasto.lisaa_varastoon(999)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_virheellisen_maaran_poisto(self):
        vanha_saldo = self.varasto.paljonko_mahtuu()

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), vanha_saldo)

    def test_ylisuuri_poisto(self):
        """Overflow of substraction.
        """
        self.varasto.ota_varastosta(999)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), self.varasto.tilavuus)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijonotulostus(self):
        """Test string method.
        """
        self.varasto.ota_varastosta(999)

        oletettu_tila = self.varasto.paljonko_mahtuu()

        self.assertEqual(str(self.varasto), f"saldo = 0.0, vielä tilaa {oletettu_tila}")
