import random
import csv
from bacteria import Bacteria
from colonia import Colonia

class Simulador():
    def __init__(self, grilla, cax, textos):
        self.__grilla = grilla
        self.__estados_grilla = [grilla]
        self.__cax = cax
        self.__textos = textos

        self.__colonia= Colonia()

    def inicializar_bacterias(self):
        interactores = [0, 0, 4, 1, 4, 1, 2, 3, 1, 3]
        
        for i in range(len(self.__grilla)):
            for j in range(len(self.__grilla[i])):
                item = random.choice(interactores) 
                
                if item == 4:
                    self.__grilla[i][j] = item
                    self.__textos[i][j].set_text(str(item) if item == 4 else '')

                if item != 0 and item != 4:  
                    self.__grilla[i][j] = item 
                    self.__textos[i][j].set_text(str(item) if item > 0 else '')
                    self.__colonia.agregar_bacteria((i, j), item) #agrega a lista de bacterias

                print(f"en {i, j} hay número {item}")
        self.__generar_csv()
        self.__estados_grilla.append(self.__grilla.copy()) 
        self.__cax.set_data(self.__grilla)
        return [self.__cax] + [t for fila in self.__textos for t in fila]

    def run(self, frame):
        # en paso pediremos el estados de la colonia para poder actualizar la grilla
        lista_bacterias = self.__colonia.paso(self.__grilla)   
        
        # Recorremos la lista de bacterias y actualizamos la información
        for bacteria in lista_bacterias:
            x, y = bacteria.get_id()
            
            bacteria_resistente = bacteria.get_resistente()
            bacteria_estado = bacteria.get_estado()
            
            # Actualizamos la grilla y el texto correspondiente
            self.__grilla[x][y] = 1
            self.__textos[x][y].set_text('1')
            
            # Si la bacteria es resistente, actualizamos su estado a 3
            if bacteria_resistente:
                self.__grilla[x][y] = 3
                self.__textos[x][y].set_text('3')
            
            # Si la bacteria está muerta, actualizamos su estado a 2
            if bacteria_estado == 2:
                self.__grilla[x][y] = 2
                self.__textos[x][y].set_text('2')
                
        self.__generar_csv()
        self.__estados_grilla.append(self.__grilla.copy()) 
        self.__cax.set_data(self.__grilla)
        return [self.__cax] + [t for fila in self.__textos for t in fila]
            
    def __generar_csv(self):
        estados = [["bacterias vivas", "bacterias resistentes", "bacterias muertas", "biofilm"]]
        for grilla in self.__estados_grilla:
            bacterias_muertas = 0
            bacterias_resistentes = 0
            bacterias_vivas = 0
            biofilm = 0
            for i in range(len(grilla)):
                for j in range(len(grilla[i])):
                    if grilla[i][j]== 1:
                        bacterias_vivas += 1
                    elif grilla[i][j] == 2:
                        bacterias_muertas += 1
                    elif grilla[i][j] == 3:
                        bacterias_resistentes += 1
                    elif grilla[i][j] == 4:
                        biofilm += 1
            estados.append([bacterias_vivas, bacterias_resistentes, bacterias_muertas, biofilm])
        with open('data_bacterias.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(estados)
                    

