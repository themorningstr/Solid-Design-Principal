#LSP :-  objects of a superclass should be able to be replaced with objects of a subclass without affecting the correctness of the program.


class Rectangle:
    def __init__(self, weight, height):
        self._height = height
        self._weight = weight


    @property
    def area(self):
        return self._weight * self._height

    def __str__(self):
        return f"Width : {self.width}, Height: {self.height}"

    

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

class Square(Rectangle):
    def __init__(self, size):
        super.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    @Rectangle.heigth.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc):
    w = rc.width
    rc.height = 10

    expected = int(w*10)
    print(f"Expected an area of {expected}, got {rc.area}")


rec = Rectangle(4,5)