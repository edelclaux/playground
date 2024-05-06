from abc import ABC, abstractmethod


class ModuleAbstract(ABC):
    @abstractmethod
    def which_module(self) -> str:
        pass

    def description(self) -> str:
        from DecoratorImport import DecoratorImport
        if DecoratorImport.is_implemented_in_module(self):
            return (
                "Module "
                + self.which_module()
                + " is decorated with "
                + self.import_coucou()
            )
        else:
            return "Module " + self.which_module() + " is raw"
