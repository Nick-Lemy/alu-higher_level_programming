#!/usr/bin/python3
import importlib.util
import sys


def print_module_names(module_file):
    # Load the module from the .pyc file
    spec = importlib.util.spec_from_file_location("hidden_module", module_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules["hidden_module"] = module
    spec.loader.exec_module(module)

    # Get all names defined in the module
    module_names = dir(module)

    # Filter names that do not start with '__'
    filtered_names = [name for name in module_names if not name.startswith('__')]

    # Sort filtered names alphabetically
    filtered_names.sort()

    # Print each name
    for name in filtered_names:
        print(name)


if __name__ == "__main__":
    # Specify the path to the compiled module hidden_4.pyc
    module_file = "./hidden_4.pyc"

    # Print the names from the module
    print_module_names(module_file)
