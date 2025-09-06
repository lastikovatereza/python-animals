# 🐾 Python Animals

Tento projekt demonstruje **objektově orientované programování (OOP)** v Pythonu skrze modelování zvířat.  
Ukazuje dědičnost, polymorfismus, abstraktní rozhraní, zapouzdření a použití `Enum` pro barvy.

## 📂 Struktura souborů

- `zvire.py` – základní třída `Zvire` (atributy, metody pro krmení, létání, výpis a zvuk).  
- `zvire_rozhrani.py` – abstraktní rozhraní `ZvireRozhrani` s metodami `mluv()` a `do_textu()`.  
- `barva.py` – výčet barev `Barva` pomocí `Enum`.  
- `kočka.py` – třídy `Kocka` a `KockaDva` (kočky s oblíbeným jídlem, zvuky).  
- `pes.py` – třída `Pes` (rasa, zvuk „Haf“).  
- `kachna.py` – třída `Kachna` (preferuje vodu, zvuk „Kvak“).  
- `demo_animals.py` – ukázkové použití všech tříd, včetně krmení, výpisu a kontrola létání.

## ✨ Funkce

- Vytvoření a manipulace se zvířaty (`Pes`, `Kočka`, `Kachna`, základní `Zvire`)  
- Zapouzdření atributů a použití property (`umi_letat`)  
- Polymorfismus a přepisování metod (`mluv`, `do_textu`)  
- Použití abstraktního rozhraní pro jednotné API  
- `Enum` pro definici barev zvířat  
