class Perro:
    def __init__(self ,  energia , hambre , estado):
        self.energia = energia
        self.hambre = hambre
        self.estado = estado


    def Comer(self,cantidad):
        if self.estado == "hambriento":
            if cantidad >=3:
                self.hambre= 0
            elif cantidad == 2:
                self.hambre= 1
            elif cantidad == 1:
                self.Hambre= 2
        print("Energia: " + str(self.energia) + " Fam: " + str(self.hambre) + " Estat del perro: " + self.estado)

    def Acariciar(self):
        print("Energia: " + str(self.energia) + " Fam: " + str(self.hambre) + " Estat del perro: " + self.estado)
        self.estado = "Contento"

    def Jugar(self):
        if self.energia <= 2 or self.hambre >= 2 or self.estado == "hambriento":
            print("El gos no vol jugar")
        else:
            self.energia -= 1
            self.hambre += 1
            self.estado = "hambriento"
            print(str("Energia: " + str(self.energia) + " Fam: " + str(self.hambre) + " Estat del perro: " + self.estado))

    def dormir(self , horas):
        if self.energia <= 2:
            self.energia += horas
            self.estat = "hambriento"
            print("Energia: " + str(self.energia) + " Hambre: " + str(self.hambre) + " Estat del perro: " + self.estado)
        else:
            print("El perro no duerme , tiene mucha energia")

