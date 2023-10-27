import random

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

# Luo kymmenen autoa satunnaisilla huippunopeuksilla
kilpaautot = []
for i in range(10):
    rekisteritunnus = "ABC-" + str(i + 1)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    kilpaautot.append(auto)

kilometritavoite = 10000
kilpailu_kaynnissa = True
tunnit = 0

while kilpailu_kaynnissa:
    for auto in kilpaautot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)  # Liikuta autoa yksi tunti

    tunnit += 1
    # Tarkistetaan, onko jokin auto saavuttanut tai ylittänyt 10 000 km
    for auto in kilpaautot:
        if auto.kuljettu_matka >= kilometritavoite:
            kilpailu_kaynnissa = False
            break

# Tulostetaan kilpailun tulokset
print("Kilpailun kesto:", tunnit, "tuntia")
print("Autot ja niiden ominaisuudet:")
for auto in kilpaautot:
    print(f"Rekisteritunnus: {auto.rekisteritunnus}, Huippunopeus: {auto.huippunopeus} km/h, Kuljettu matka: {auto.kuljettu_matka} km")
