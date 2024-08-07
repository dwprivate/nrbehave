import os
import pkgutil

# add other steps to auto load

# this snippet load steps from subdirectories:
__all__ = []
PATH = [os.path.dirname(__file__)]
for loader, module_name, is_pkg in pkgutil.walk_packages(PATH):
    __all__.append(module_name)
    _module = loader.find_module(module_name).load_module(module_name)
    globals()[module_name] = _module
