class Vetor3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def soma(u, v):
        return (u.x+v.x, u.y+v.y, u.z+v.z)


class Vetor2D(Vetor3D):
    def __init__(self, x, y):
        super().__init__(x, y, 0)

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)


def somar_vetores(u, v):
    return v.__class__.soma(u, v)

print(somar_vetores(Vetor2D(1, 2), Vetor3D(3, 4, 5)))
print(somar_vetores(Vetor2D(1, 2), Vetor2D(-1, 7)))
print(somar_vetores(Vetor3D(1, 2, 3), Vetor3D(4, 5, -23)))