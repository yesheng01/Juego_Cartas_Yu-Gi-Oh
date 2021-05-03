"""
dsadasd
dasdsad
dasdasd
"""

#Print es como un sout en Java

print("Hello World")


x = 110
y = "Sheng"
print(x , y)
print(x)
print(y)
#Conversion srt de esta forma se puede mostrar en numero
print(str(x) + " " + y)
x , y ,z = "pedro" , 144 , "amalaor"
print(x , y , z)

#Funciones
p = "pr"
def Nombre():
    p = "dsada"
    print(p)
Nombre()
print(p)


print(type(x))


x = int(1)
y = int(2.0)
z = int("3")

print(x)
print(y)
print(z)

a = "aa \n aa"
print(a)

a = "Sheng"
print(a[4])
print(len(a))


for x in "Sheng":
    print(x)



a = "pera"
for x in a:
    print(x)


a = "dsakldbhaifhaiofghaioghfoghoaghioahgodhgiosdhgiosdhgioshgsighsdioghiosdhgisodhgi"
print(a.replace("a" , "i").replace("o" , "e"))


a= "Hola Sheng"
print(a.split(" "))


cantidad = 3
item = "pera"
precio = 22.8
txt = "Quiero tener {} lo que sea {} de lo que se dice {}"
print(txt.format(cantidad , item , precio))

print(2==2)
print(2<0)


a = 10
b = 10
if  (a>b):
    print("a es mayor que el del b")
elif(b>a):
    print("b es mayor que a ")
elif(b==a):
    print("es igual")



x = input("Introduce tu nombre: ")
print(x)

def suma(a,b):
    return a+b

x=2
y=3
print(suma(x,y))

import random

z = random.randint(0,100)
print(z)