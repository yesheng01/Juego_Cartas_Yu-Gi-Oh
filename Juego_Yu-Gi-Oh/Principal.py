from Engine import Juego

jugar = True

while jugar:
    j1 = Juego("*********Yu-Gi-Oh*********")
    j1.Personaje_Tecnica()
    j1.mostrar()
    j1.Elegir_Personaje()
    j1.ElegirCPU()
    j1.lucha()
    jugar = j1.volverJugar()