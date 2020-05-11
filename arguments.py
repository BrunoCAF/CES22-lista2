#96-98

def calculadora(*args, **kwargs):
    for k in kwargs.keys():
        print(kwargs[k](args))
    return

# Exemplos
calculadora(1, 2, 3, 4, 5, 6, 7, 
            op1 = lambda l: sum(x for x in l), 
            op2 = lambda l: max(x for x in l),
            op3 = lambda l: l[1]*l[3] + l[5]**2)