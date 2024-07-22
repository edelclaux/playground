# from ModuleOcchab import ModuleOcchab
# from ModuleSynthese import ModuleSynthese
# from ModuleMetadata import ModuleMetadata

# module_occhab = ModuleOcchab()
# print(f"{module_occhab.description()}\n")

# module_synthese = ModuleSynthese()
# print(f"{module_synthese.description()}\n")

# module_metadata = ModuleMetadata()
# print(f"{module_metadata.description()}\n")

from MethodWithAttribute import Module
module = Module()
print(module.method())
print(module.method.label)

attr = getattr(module.method, "object_code", "ALL")
print(attr)
