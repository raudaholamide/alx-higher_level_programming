#!/usr/bin/python3
def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, encoding='utf-8') as o_file:
        read_f = o_file.read()
    print(read_f, end="")
