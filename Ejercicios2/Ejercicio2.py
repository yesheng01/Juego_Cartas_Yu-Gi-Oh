
''' Atributos '''
servicios=4000
precio1=65
precio2=70
precio3=95
precio4=115

''' Atributo para preguntar al usuario '''
alumnos= int(input("Total de alumno que van al viaje: "))


''' Primer metodo calculo de los alumnos '''

def calculo1(alumnos):

    importeA=servicios/alumnos
    if alumnos>=100:
        importeSubTotal=importeA+precio1
        print("Optas el precio de 65")
    elif alumnos <= 99 and alumnos >= 50:
        importeSubTotal=importeA+precio2
        print("Optas el precio de  70")
    elif alumnos<=49 and alumnos>=30:
        importeSubTotal=importeA+precio3
        print("Optas el precio de  95")
    elif alumnos <= 29:
        importeSubTotal=importeA+precio4
        print("Optas el precio de  115")

    return importeSubTotal

''' Segundo metodo calculo de los agencias '''

def calculo2(alumnos):
    if alumnos>=100:
        precio=precio1*alumnos
    elif alumnos <= 99 and alumnos >= 50:
        precio=precio2*alumnos
    elif alumnos <= 49 and alumnos >= 30:
        precio=precio3*alumnos
    elif alumnos <= 29:
        precio=precio4*alumnos

    importeSubTotal=servicios+precio
    return importeSubTotal


importes=calculo1(alumnos)
totalApagar=calculo2(alumnos)
print("Total a pagar a la agencia: "+str(totalApagar)+"€ ")
print("importe por alumno: "+str(importes)+"€")