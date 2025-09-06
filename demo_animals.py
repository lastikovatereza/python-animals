from kachna import Kachna
from kočka import Kocka
from pes import Pes
from zvire import Zvire

# Vytvoříme zvířata
sova = Zvire("Sova", 8.5, "pták", "hnědá")
orel = Zvire("Orel", 12, "dravý pták", "černá")

# Výpis
sova.vypis()
orel.vypis()

# Krmení sovy
sova.nakrm(1)
sova.vypis()

# Zjištění, zda umí létat
print(f"{sova.jmeno} umí létat? {'Ano' if sova.get_umi_letat() else 'Ne'}")

zvirata = [
    Kocka("Micka", 4, "bílá", "losos"),
    Pes("Rex", 15, "hnědý", "labrador"),
    Kachna("Kvakalka", 3, "zelená", True)
]

for zvire in zvirata:
    print(zvire.do_textu())
