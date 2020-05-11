#80-85

class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:

    def plot(self, ratio, topleft):
        # ...
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

class Quadrilateral(Polygon):
    geometric_type = 'Quadrilateral'

class Rectangle(Quadrilateral):
    geometric_type = 'Rectangle'
    def __init__(self, base, height):
        self.base, self.height = base, height

    def area(self):
        return self.base * self.height

    def diagonal(self):
        return (self.base**2 + self.height**2) ** .5

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon):
    geometric_type = 'Regular Hexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(Rectangle, RegularPolygon):
    geometric_type = 'Square'

    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.side * self.side


print(Square.mro())
print(Square(7).diagonal())