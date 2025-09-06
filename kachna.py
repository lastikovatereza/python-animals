from zvire import Zvire


class Kachna(Zvire):
    def __init__(self, jmeno, vaha, barva, ma_rad_vodu):
        super().__init__(jmeno, vaha, "Kachna", barva)
        self.ma_rad_vodu = ma_rad_vodu

    def mluv(self):
        return "Kvak"
