#OPC :- Open Closed Principal Open for extenstion Closed for modification


from enum import Enum


class Color(Enum):
    RED=1
    GREEN=2
    BLUE=3



class Size(Enum):
    SMALL=1
    MEDIUM=2
    LARGE=3


class Product:
    def __init__(self, name, color, size):
        self.name=name
        self.color=color
        self.size=size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p


    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    
    def filter_by_size_and_color(self , products, size, color):
        for p in products:
            if p.color == color and p.size==size:
                yield p



class Specification:
    def is_statisfied(slef, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass



class ColorSpectification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color  == self.color



class SizeSpectification(Specification):
    def __init__(self, size):
        self.size = size

    def is_statisfied(self, item):
        return item.size  == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item




if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.GREEN, Size.LARGE)



    product = [apple, tree, house]


    pf = ProductFilter()
    print()


    
