class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        etenyt_matka = self.tamanhetkinen_nopeus * tuntimaara
        self.kuljettu_matka += etenyt_matka


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki_koko = bensatankki_koko


sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdyta(150)  # Asetetaan nopeus
polttomoottoriauto.kiihdyta(140)  # Asetetaan nopeus

# Käske autoja ajamaan 3 tuntia
sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

# Tulosta autojen matkamittarilukemat
print("Sähköauton kuljettu matka:", sähköauto.kuljettu_matka, "km")
print("Polttomoottoriauton kuljettu matka:", polttomoottoriauto.kuljettu_matka, "km")
