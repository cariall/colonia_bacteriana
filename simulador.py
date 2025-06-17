import random
import csv

class Simulador():
    def __init__(self, grilla, cax, textos):
        self.__grilla = grilla
        self.__estados_grilla = [grilla]
        self.__cax = cax
        self.__textos = textos

    def run(self, frame):
        interactores = [0, 0, 0, 4, 1, 1, 2, 3, 1, 3]
        for i in range(len(self.__grilla)):
            for j in range(len(self.__grilla[i])):
                item = random.choice(interactores)
                if item != 0:
                    self.__grilla[i, j] = item 
                    self.__textos[i][j].set_text(str(item) if item > 0 else '')
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
                    

