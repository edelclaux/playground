from ModuleAbstract import ModuleAbstract
from ImportSynthese import ImportSynthese


class ModuleSynthese(ModuleAbstract):
    def __init__(self) -> None:
        self._import = ImportSynthese()

    def which_module(self) -> str:
        return "Module Synthèse"
