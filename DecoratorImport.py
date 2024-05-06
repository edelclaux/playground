from ModuleAbstract import ModuleAbstract
from DecoratorAbstract import DecoratorAbstract
from abc import abstractmethod


class DecoratorImport(DecoratorAbstract):
    @abstractmethod
    def import_coucou(self) -> str:
        pass
