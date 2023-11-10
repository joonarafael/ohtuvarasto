"""This is the Varasto class.
"""

class Varasto:
    """Class object to handle a Varasto.
    """
    def __init__(self, tilavuus: float or int, alku_saldo = 0):
        """Initialize the Varasto object.

        Args:
            tilavuus: Desired maximum capacity.
            alku_saldo (int, optional): Starting volume as an int. Defaults to 0.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            self.saldo = 0.0

        elif alku_saldo <= tilavuus:
            self.saldo = alku_saldo

        else:
            self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """Return the available capacity.

        Returns:
            float: Available capacity as a float.
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara: float or int):
        """Method to add volume to the Varasto object.

        Args:
            maara: Amount to be added.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara: float or int):
        """Method to take balance out of from the Varasto.

        Args:
            maara: Requested amount to be taken out.

        Returns:
            float: Actual amount that was taken from the Varasto.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
