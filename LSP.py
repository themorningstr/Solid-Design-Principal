#LSP :-  objects of a superclass should be able to be replaced with objects of a subclass without affecting the correctness of the program.


class Rectangle:
    def __init__(self, weight, height):
        self._height = height
        self._weight = weight

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        return setattr(self._width , value)
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        return setattr(self._height, value)

        