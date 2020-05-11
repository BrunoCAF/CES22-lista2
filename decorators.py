def matrix_decorate(T):
    def wrapper(x, y, z):
        c1, c2, c3 = T(1,0,0), T(0,1,0), T(0,0,1)
        vector = (x, y, z)
        rows = len(c1)
        disp = ""
        for r in range(max(rows, 3)):
            if r < rows:
                disp += ("[{0:>4.1f} {1:>4.1f} {2:>4.1f}]").format(c1[r], c2[r], c3[r])
            else:
                disp += " "*16
            disp += ("*" if r == 1 else " ")
            if r < 3:
                disp += ("[{0:>4.1f}]").format(vector[r])
            else:
                disp += " "*6
            disp += (" = " if r == 1 else " "*3)
            if r < rows:
                disp += ("[{0:>4.1f}]").format(T(x,y,z)[r])
            else:
                disp += " "*6
            disp += "\n"
        print(disp)
    return wrapper

@matrix_decorate
def T1(x, y, z):
    return (3*x - y + 5*z, x + y, 2*z, x+y+2*z, -x)

@matrix_decorate
def T2(x, y, z):
    return (3*x - y + 5*z, x + y, 2*z)

@matrix_decorate
def T3(x, y, z):
    return (3*x - y + 5*z, x + y)

T1(1,2,3)
T2(1,2,3)
T3(1,2,3)