#55-70
# Lets illustrate the use of static, class and abstract methods by modelling Polygons

import abc, turtle
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def distance(A, B):
        return sqrt((A.x - B.x)**2 + (A.y - B.y)**2)

    def norm(self):
        return self.distance(self, Point(0,0))


class GridPoint(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    @staticmethod
    def distance(A, B):
        return abs(A.x - B.x) + abs(A.y - B.y)


class Polygon:
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, list_of_points):
        self.points = list_of_points

    @abc.abstractmethod
    def calculate_perimeter(self):
        n = len(self.points)
        return sum(Point.distance(self.points[i], self.points[(i+1)%n]) for i in range(n))

    @abc.abstractmethod
    def calculate_area(self):
        """Calculate the polygon's area"""



class Triangle(Polygon):
    n = 3
    def __init__(self, P1, P2, P3):
        super().__init__([P1, P2, P3])

    @classmethod
    def number_of_sides(cls):
        return cls.n
    
    @classmethod
    def corner_triangle(cls, a, b):
        return cls(Point(0, 0), Point(a, 0), Point(0, b))

    def calculate_area(self):
        return abs(P1.x*P2.y-P1.y*P2.x + P2.x*P3.y-P2.y*P3.x + P3.x*P1.y-P3.y*P1.x)/2
    

print(GridPoint(2, 4).norm())
print(Triangle.number_of_sides())
print(Triangle.corner_triangle(2, 5).calculate_perimeter())
print(Polygon([Point(0, 0), Point(2, 0), Point(0, 5)]).calculate_perimeter())
