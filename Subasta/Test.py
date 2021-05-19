from Usuario import Usuari
from Subasta import Subasta


class Test:
    Toni = Usuari("Toni", 100)
    Pep = Usuari("Pep", 150)
    Enric = Usuari("Enric", 300)

    pj1 = Subasta("Telefono Movil", Toni)

    print(str(pj1.Pujar(Pep, 100)))
    print(str(pj1.getPujasaMayor()))

    print(str(pj1.Pujar(Enric, 50)))
    print(str(pj1.Pujar(Enric, 150)))
    print(str(pj1.getPujasaMayor()))
    print(str(pj1.getHistorial()))
    print(str(pj1.Ejecutar()))
    print(str(pj1.Pujar(Enric, 200)))
    pj2 = Subasta("Impresora 3D", Pep)
    print(str(pj2.PujarUsuario(Enric)))
    print(str(pj2.Ejecutar()))
    print(str(pj1.getHistorial()))
    print(str(pj2.getHistorial()))

    usuaris = [Toni, Pep, Enric]
    for usuari in usuaris:
        print("Usuario : " + str(usuari))
        print("El dinero actual de este usuario es :  " + str(usuari.getDinero()))