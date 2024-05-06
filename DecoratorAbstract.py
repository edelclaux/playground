from ModuleAbstract import ModuleAbstract
from abc import ABC

class DecoratorAbstract(ABC):
    _module: ModuleAbstract = None
    def __init__(self, module: ModuleAbstract) -> None:
        self._module = module

    @classmethod
    def is_implemented_in_module(cls, module: ModuleAbstract) -> bool:
        return isinstance(module, cls)
