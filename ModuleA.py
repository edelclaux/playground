from ModuleAbstract import ModuleAbstract
from DecoratorImport import DecoratorImport


class ModuleA(ModuleAbstract, DecoratorImport):

    def __init__(self) -> None:
        super(DecoratorImport, self).__init__(self)

    def which_module(self) -> str:
        return "Module A"

    def import_coucou(self) -> str:
        return "Import A"
