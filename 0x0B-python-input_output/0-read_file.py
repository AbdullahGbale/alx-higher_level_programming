#!/usr/bin/python3
  """Defines text file-read function."""


def read_file(filename=""):
    """Prints content of a UTF8 text file to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

read_file("example.txt")
