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

auto1 = Auto("ABC-123", 142)
print("Rekisteritunnus:", auto1.rekisteritunnus)
print("Huippunopeus:", auto1.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", auto1.tamanhetkinen_nopeus, "km/h")
print("Kuljettu matka:", auto1.kuljettu_matka, "km")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print("Nopeus kiihdyttämisen jälkeen:", auto1.tamanhetkinen_nopeus, "km/h")

auto1.kulje(1.5)
print("Kuljetun matkan jälkeen:", auto1.kuljettu_matka, "km")
