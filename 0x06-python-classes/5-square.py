#!/usr/bin/python3
# A class Square that defines a square


class Square:
    def __init__(self, size=0):  # init allow square class to be used
        self.__size = size   # asign private instance attribute size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size is not 0:
            for i in range(self.__size):
                print("{}".format("#" * self.__size))
        else:
            print()
