from ModuleAbstract import ModuleAbstract
from ImportOcchab import ImportOcchab

class ModuleOcchab(ModuleAbstract):
    def __init__(self):
        self._import = ImportOcchab()
        
    def which_module(self) -> str:
        return "Module Occhab"
