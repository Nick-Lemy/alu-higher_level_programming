#!/usr/bin/python3
import importlib.util
import sys
def print_module_names(module_file):
    spec = importlib.util.spec_from_file_location("hidden_module", module_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules["hidden_module"] = module
    spec.loader.exec_module(module)
    module_names = dir(module)
    for name in module_names:
        filtered_names = sorted(name)
    #filtered_names = sorted(name for name in module_names if not name.startswith('__'))
    for name in filtered_names:
        print(name)
if __name__ == "__main__":
    module_file = "./hidden_4.pyc"
    print_module_names(module_file)

