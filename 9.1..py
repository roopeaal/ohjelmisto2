class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0


uusi_auto = Auto("ABC-123", 142)
print("Rekisteritunnus:", uusi_auto.rekisteritunnus)
print("Huippunopeus:", uusi_auto.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", uusi_auto.tamanhetkinen_nopeus, "km/h")
print("Kuljettu matka:", uusi_auto.kuljettu_matka, "km")
