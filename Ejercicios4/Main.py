from sobre import sobre
from cartas import cartas

c1 = cartas("Oshiris", "Divino", "Legendaria rara",10 , 10, 5, "SKY DRAGON")
c2 = cartas("Obelix", "Divino", "Legendaria rara", 10, 10, 10, "THE TORMENTOR")
c3 = cartas("Sliffer", "Divino", "Legendaria rara", 10, 10, 7, "DRAGON")
c4 = cartas("Uria", "Divino", "Legendaria rara", 10, 10, 10, "LORD OF SEARING FLAMES")
c5 = cartas("Hamon", "Divino", "Legendaria rara", 10, 10, 8, "LORD OF STRIKING THUNDER")

s1 = sobre("YU-GI-OH", "YU-GI-OH , Juegos de Cartas", 1)


s1.ObtenerCartas(c1)
s1.ObtenerCartas(c2)
s1.ObtenerCartas(c3)
s1.ObtenerCartas(c4)
s1.ObtenerCartas(c5)
s1.VeureCartesSobre()