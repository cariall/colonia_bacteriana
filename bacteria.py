class Bacteria():
    def __init__(self, id, raza, energia, resistente, estado):
        self.__id = id
        self.__raza = raza
        self.__energia = energia
        self.__resistente = resistente
        self.__estado = estado        

    def alimentar(self, numero):
        if self.__energia > 15:
            print("Bacteria lista para reproducción")
        else: 
            print("Bacteria absorbiendo nutrientes")

    def dividirse():
        pass

    def mutar():
        pass

    def morir():
        pass

