from zvire import Zvire


class Pes(Zvire):
    def __init__(self, jmeno, vaha, barva, rasa):
        super().__init__(jmeno, vaha, "Pes", barva)
        self.rasa = rasa

    def mluv(self):
        return "Haf"
