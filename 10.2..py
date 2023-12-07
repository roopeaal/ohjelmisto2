class Hissi:
    def __init__(self, alin_kerros, ylimm_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimm_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print("Hissi on kerroksessa", self.kerros)

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros < kohde_kerros:
            self.kerros_ylös()
        while self.kerros > kohde_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylimm_kerros, hissien_lukumäärä):
        self.hissit = [Hissi(alin_kerros, ylimm_kerros) for _ in range(hissien_lukumäärä)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero ei ole kelvollinen.")

talo = Talo(1, 10, 3)

# Aja hissejä eri kerroksiin
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)

# Kokeile hissinumeron virheellistä antamista
talo.aja_hissiä(3, 3)
