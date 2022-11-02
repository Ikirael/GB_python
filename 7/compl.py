def comp():
    r1 = float(input("re 1: "))
    j1 = float(input("im 1: "))
    return complex(r1,j1)

def add():
    return comp() + comp()

def sub():
    return comp() - comp()

def mul():
    return comp() * comp()

def div():
    return comp() / comp()