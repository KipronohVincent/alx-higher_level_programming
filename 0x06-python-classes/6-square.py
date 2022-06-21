#!/usr/bin/python3
""" Creating a square class """


class Square:
    """ Defining a class square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializing a square class
        Args: size=0: size of the square
        Args: position=(0, 0): position of the square
         """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getting the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getting the position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setting the position of the square """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculating the area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """ Printing the square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
