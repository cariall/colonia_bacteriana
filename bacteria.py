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
        
    def dividirse():
        pass
    
    def mutar():
        pass

    def morir():
        pass
    
    def get_id(self):
        return self.__id 
    
    def get_raza(self):
        return self.__raza
    
    def get_energia(self):
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