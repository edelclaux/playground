from abc import ABC, abstractmethod
from ImportAbstract import ImportAbstract as Import

class ModuleAbstract(ABC):
    _import: Import = None

    @abstractmethod
    def which_module(self) -> str:
        pass

    def description(self) -> str:
        if self.is_import_implemented():
            return "Module '" + self.which_module() + "' has the following import in its composition: '" + self._import.which_import() + "'"
        else:
            return "Module '" + self.which_module() + "' has no import."

    def is_import_implemented(self) -> bool:
        return self._import != None
