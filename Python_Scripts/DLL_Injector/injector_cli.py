# Good Example of a DLL Injector
# Developed by -> numaru / https://github.com/numaru

import sys

from injector import Injector


def main():
    path_exe = str(sys.argv[1])
    path_dll = str(sys.argv[2])

    injector = Injector()
    pid = injector.create_process(path_exe)
    injector.load_from_pid(pid)
    injector.inject_dll(path_dll)
    injector.unload()

if __name__ == "__main__":
    main()