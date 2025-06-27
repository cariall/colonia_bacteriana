import random
class Bacteria():
    def __init__(self, id, raza, energia, resistente, estado):
        self.__id = id
        self.__raza = raza
        self.__energia = energia
        self.__resistente = resistente
        self.__estado = estado       
    
    def alimentar(self, cantidad):
        self.__energia += cantidad
        return self.__energia
        
    def dividirse(self): #es una copia de la bacteria original que alcanzó nivel de energía
        return Bacteria(self.__id, self.__raza, self.__energia // 2, self.__resistente, self.__estado)
    
    def mutar(self):
        self.__estado = 3
        return self.__estado

    def morir(self):
        self.__estado = 2
        self.__energia = 0
        return self.__estado, self.__energia
    
    def get_id(self):
        return self.__id 
    
    def set_id(self, nuevo_id):
        self.__id = nuevo_id
        return self.__id
    
    def get_energia(self):
        return self.__energia
    
    def set_energia(self, cantidad):
        self.__energia = cantidad
        if self.__energia < 1:
            self.__energia = 0
        return self.__energia 
    
    def get_resistente(self):
        return self.__resistente
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado
        return self.__estado

    def obtener_datos(self):
        cadena = (f"id: {self.__id}, raza: {self.__raza}, energía: {self.__energia}, resistencia: {self.__resistente}, estado: {self.__estado} ")
        return cadena