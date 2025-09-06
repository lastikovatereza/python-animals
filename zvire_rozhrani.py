from abc import ABC, abstractmethod

class ZvireRozhrani(ABC):
    @abstractmethod
    def mluv(self) -> str:
        """Vrátí zvuk, který zvíře vydává."""
        pass

    @abstractmethod
    def do_textu(self) -> str:
        """Vrátí textovou reprezentaci zvířete."""
        pass