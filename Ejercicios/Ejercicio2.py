num1 = int(input("Introduzca un numero entre el 0 y el 100: "))
num2 = int(input("Introduzca otro numero entre el 0 y el 100:    "))
elige = input("a = suma, b = resta, c = multiplicacion , d =dividir :   ")
def switch(case, a, b):
    if case == "a":
        print(a + b)
    elif case == "b":
        print(a - b)
    elif case == "c":
        print(a * b)
    elif case == "d":
        print(a % b)
switch(elige, num1, num2)