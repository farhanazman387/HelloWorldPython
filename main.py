# is a note to myself.
# import importlib
# importlib.import_module("Hello")
# importlib.import_module('World')
from Hello import hello
from World import world


def print_hi(name):  # this is how to write the function
    print(f'{name}')  # this is how you write the comment always starts with #
    first = hello()
    second = world()
    final = first + second
    print(final)
    exit()


# there should be 2X space after every def or the beginning of def
if __name__ == '__main__':
    print_hi('Good Morning')