class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self):    # All we have done is renamed the method
            return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def reflect_x(self):
        return Point(self.x, -self.y)

    def slope_from_origin(self):
        return self.y/self.x if self.x != 0 else "Infty"

    def get_line_to(self, target):
        x1, x2, y1, y2 = self.x, target.x, self.y, target.y
        return ((y1 - y2)/(x1 - x2), (y1*x2 - y2*x1)/(x2 - x1))


print(Point(4, 11).get_line_to(Point(6, 15)))