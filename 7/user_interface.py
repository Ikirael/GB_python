import ration
import excep
import ration
import compl

def operations(i):
    if i == 1:
        print("Operations:", "1 - sum", "2 - sub", "3 - mul", "4 - div", "5 - pow", "6 - sqrt", "0 - previous menu", sep='\n')
    if i == 2:
        print("Operations:", "1 - sum", "2 - sub", "3 - mul", "4 - div", "0 - previous menu", sep='\n')
    
def compl_menu():
    operations(2)
    c = int(input(": "))
    if c == 1:
        print(compl.add())
    elif c == 2:
        print(compl.sub())
    elif c == 3:
        print(compl.mul())
    elif c == 4:
        print(compl.div())
    elif c == 0:
        menu()
    else:
        excep.wrong_number()
        compl_menu()
    menu()


def rat_menu():
    operations(1)
    c = int(input(": "))
    if c == 1:
        print(ration.add())
    elif c == 2:
        print(ration.sub())
    elif c == 3:
        print(ration.mul())
    elif c == 4:
        print(ration.div())
    elif c == 5:
        print(ration.pow())
    elif c == 6:
        print(ration.sqrtt())
    elif c == 0:
        menu()
    else:
        excep.wrong_number()
        rat_menu()
    menu()

def menu():
    print("Calculacor welcomes you!\n")
    print("Working with:", "1 - rational", "2 - complex", "0 - exit", sep='\n')
    c = int(input(": "))
    if c == 1:
        rat_menu()
    elif c == 2:
        compl_menu()
    elif c == 0:
        return 1
    else:
        excep.wrong_number()
        menu()

