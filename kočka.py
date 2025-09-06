from barva import Barva
from zvire import Zvire
from zvire_rozhrani import ZvireRozhrani


class Kocka(Zvire):
    def __init__(self, jmeno, vaha, barva: Barva, oblibene_jidlo):
        super().__init__(jmeno, vaha, "Kočka", barva)
        self.oblibene_jidlo = oblibene_jidlo

    def mluv(self):
        return "Mňau"

class KockaDva(ZvireRozhrani):
    def __init__(self, jmeno, vaha, barva):
        self.jmeno = jmeno
        self.vaha = vaha
        self.barva = barva

    def mluv(self) -> str:
        return "Mňau"

    def do_textu(self) -> str:
        return f"{self.jmeno} ({self.barva}, {self.vaha} kg) říká: {self.mluv()}"
