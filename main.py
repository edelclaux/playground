from ModuleOcchab import ModuleOcchab
from ModuleSynthese import ModuleSynthese
from ModuleMetadata import ModuleMetadata

print('\n')

module_occhab = ModuleOcchab()
print(f"{module_occhab.description()}\n")

module_synthese = ModuleSynthese()
print(f"{module_synthese.description()}\n")

module_metadata = ModuleMetadata()
print(f"{module_metadata.description()}\n")
