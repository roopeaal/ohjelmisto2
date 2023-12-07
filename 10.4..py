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

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailu: {self.nimi}")
        print(f"{'Rekisteritunnus':<12}{'Nopeus (km/h)':<15}{'Matka (km)':<15}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12}{auto.tamanhetkinen_nopeus:<15}{auto.kuljettu_matka:<15}")
        print("\n")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

kilpaautot = []
for i in range(10):
    rekisteritunnus = "ABC-" + str(i + 1)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    kilpaautot.append(auto)

suuri_romuralli = Kilpailu("Suuri romuralli", 8000, kilpaautot)
tunnit = 0

while not suuri_romuralli.kilpailu_ohi():
    suuri_romuralli.tunti_kuluu()
    if tunnit % 10 == 0:  # Tulostetaan tilanne 10 tunnin välein
        suuri_romuralli.tulosta_tilanne()
    tunnit += 1

suuri_romuralli.tulosta_tilanne()  # Tulostetaan lopputilanne
print(f"Kilpailu päättyi {tunnit} tunnin jälkeen.")
