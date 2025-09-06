
class Zvire:
    def __init__(self, jmeno, vaha, druh, barva):
        self.jmeno = jmeno
        self.vaha = vaha  # v kg
        self.druh = druh
        self.barva = barva
        self._umi_letat = self.vaha >= 9  # zapouzdřený atribut

    def nakrm(self, mnozstvi):
        if mnozstvi > 0:
            self.vaha += mnozstvi
            print(f"{self.jmeno} byl(a) nakrmen(a) o {mnozstvi} kg.")
            self._umi_letat = self.vaha >= 9  # přepočítání podle nové váhy
        else:
            print("Nelze nakrmit zápornou nebo nulovou hodnotou.")

    # property – přístup jako k atributu
    @property
    def umi_letat(self):
        return self.vaha >= 9

    # klasický getter – přístup jako metoda
    def get_umi_letat(self):
        return self._umi_letat

    def vypis(self):
        letani = "ano" if self.get_umi_letat() else "ne"
        print(f"{self.jmeno} ({self.druh}, {self.barva}) váží {self.vaha} kg. Umí létat: {letani}")

    def mluv(self):
        return ""

    def do_textu(self):
        return f"{self.jmeno} ({self.druh}, {self.barva}) váží {self.vaha} kg a říká: {self.mluv()}"