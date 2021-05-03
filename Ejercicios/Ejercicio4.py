import random

z = random.randint(0,10)
o = int (input ("Introduce un numero a adivinar: "))
if  o == z :
    print("Has adivinado el numero , el numero era : ")
    print(z)
else:
    print("No has adivinado el numero")