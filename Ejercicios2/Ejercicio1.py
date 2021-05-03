
''' Primer metodo calculo de precio'''
def calculoPrecio(tipo,tamaño):
    if tipo == "A":
        if tamaño == "1":
            return 20
        else:
            return 30
    if tipo == "B":
        if tamaño == "1":
            return 30
        else:
            return 50
''' Segundo metodo Menu'''
def Switch():
    tipo = input("Elige lo A or B: ")
    tamaño = input("Elige el tamaño 1 o 2: ")
    cantidad = int(input("Cuantos productos quieres añadirle: "))
    PrecioFinal =cantidad * calculoPrecio(tipo, tamaño)
    print("Debes pagar : " + str(PrecioFinal)+"€")

Switch()