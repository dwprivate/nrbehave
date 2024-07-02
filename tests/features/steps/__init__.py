# DO NOT DELETE, RENAME NOR ALTER THIS FILE
import os
import pkgutil

from nrbehave import steps

# this snippet load steps from subdirectories:

# DWI TODO organiser les steps
# __all__ = []
# PATH = [os.path.dirname(__file__)]
# for loader, module_name, is_pkg in pkgutil.walk_packages(PATH):
#     __all__.append(module_name)
#     _module = loader.find_module(module_name).load_module(module_name)
#     globals()[module_name] = _module
