class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus  # Ei ylitetä huippunopeutta
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0  # Ei sallita negatiivista nopeutta
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

uusi_auto = Auto("ABC-123", 142)
print("Rekisteritunnus:", uusi_auto.rekisteritunnus)
print("Huippunopeus:", uusi_auto.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", uusi_auto.tamanhetkinen_nopeus, "km/h")
print("Kuljettu matka:", uusi_auto.kuljettu_matka, "km")

auto1 = Auto("ABC-123", 142)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print("Nopeus kiihdyttämisen jälkeen:", auto1.tamanhetkinen_nopeus, "km/h")

auto1.kiihdyta(-200)
print("Nopeus hätäjarrutuksen jälkeen:", auto1.tamanhetkinen_nopeus, "km/h")
