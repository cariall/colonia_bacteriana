import random
from bacteria import Bacteria
import csv
from ambiente import Ambiente
class Colonia():
    def __init__(self):
        self.__lista_bacterias = []
        self.__ambiente = Ambiente(10, 10)

    def agregar_bacteria(self, coordenadas, item):
        resistencia = 3 #porque el número 3 significa resistente
        raza = ["Curt", "Mop", "Cray", "Hunt", "Hert"]
        energia = [10, 20, 40, 60, 80, 100]
        raza_elegida = random.choice(raza)
        nivel_energia = random.choice(energia)
        resistencia_elegida = True

        if item != resistencia:
            resistencia_elegida = False
            
        if item == 2:
            nivel_energia = 0

        bacteria = Bacteria(coordenadas, raza_elegida, nivel_energia, resistencia_elegida, item)
        self.__lista_bacterias.append(bacteria)

    def modificar_ambiente(self, grilla):
        grilla = self.__ambiente.aplicar_ambiente(grilla)
        return grilla

    def paso(self, grilla):
        bacterias_antiguas = self.__lista_bacterias
        energia_mitosis = 80
        alimento = random.randint(15,25)

        for bacteria in bacterias_antiguas: #[Bacteria, Bacteria, Bacteria]
            x,y  = bacteria.get_id() #[Bacteria.id()]
            contador = 0

            if bacteria.get_estado() == 2: 
                grilla[x][y] = 2 

            if bacteria.get_estado() == 3 or bacteria.get_estado() == 1: 
                vecinos = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]

                for nx, ny in vecinos:
                    if 0 <= nx < len(grilla) and 0 <= ny < len(grilla[0]): #si x es mayor a 0 o menos a longitud de la grilla
                        if grilla[nx][ny] == 4: #si coordenadas concuerdan con 4
                            bacteria.alimentar(alimento)
                            self.__ambiente.consumir_nutriente(nx, ny, alimento)
                            grilla[nx][ny] == 0 #Biofilm desaparece
                        else: #si no concuerdan con 4
                            contador += 1

                            if contador == 4:
                                energia_actual = bacteria.set_energia(bacteria.get_energia() - 10) 

            if bacteria.get_energia() <= 5:
                bacteria.morir()
        
            if bacteria.get_energia() >= energia_mitosis and (bacteria.get_estado() == 1 or bacteria.get_estado() == 3):
                print(f"Bacteria en {x, y} tiene suficiente energía para dividirse")
                random.shuffle(vecinos)  # Para que la hija no siempre vaya al mismo lugar
                for nx, ny in vecinos:
                    if 0 <= nx < len(grilla) and 0 <= ny < len(grilla[0]) and grilla[nx][ny] == 0: # si la coordenada está dentro de los límites de la grilla y es un espacio vacío o muerto
                        nueva_bacteria = bacteria.dividirse((nx, ny))
                        self.__lista_bacterias.append(nueva_bacteria)
                        grilla[nx][ny] = nueva_bacteria.get_estado()
                        bacteria.set_energia(bacteria.get_energia() // 2)

                        if not nueva_bacteria.get_estado() == 3:
                            probabilidad_heredar_resistencia = 0.5
                            if random.random() > probabilidad_heredar_resistencia:
                                nueva_bacteria.set_estado(bacteria.get_estado()) 
                                print(f"Bacteria en {nueva_bacteria.get_id()} heredó (estado: {nueva_bacteria.get_estado()})")
                            else: 
                                print(f"Bacteria en {nueva_bacteria.get_id()} no heredó (estado: {nueva_bacteria.get_estado()})")

                            probabilidad_mutacion = 0.30
                            if random.random() < probabilidad_mutacion:
                                nueva_bacteria.mutar()
                                print(f"Bacteria en {nueva_bacteria.get_id()} mutó (estado: {nueva_bacteria.get_estado()}) ")
                            else:
                                print(f"Bacteria en {nueva_bacteria.get_id()} no ha mutado")
                    
                        print(f"Bacteria en {x, y} crea una hija en {nx, ny}")
                        break  # Solo una división por ciclo
        
            grilla[x][y] = bacteria.get_estado() #Actualiza la grilla

        return bacterias_antiguas
        
    def reporte_estado(self, grilla):
        bacterias_vivas = 0
        bacterias_resistentes = 0
        bacterias_muertas = 0
        biofilm = 0
        for i in range(len(grilla)):
            for j in range(len(grilla[i])):
                if grilla[i][j] == 1:
                    bacterias_vivas += 1
                elif grilla[i][j] == 2:
                    bacterias_muertas += 1
                elif grilla[i][j] == 3:
                    bacterias_resistentes += 1
                elif grilla[i][j] == 4:
                    biofilm += 1
        return {
            "Bacterias vivas": bacterias_vivas,
            "bacterias resistentes": bacterias_resistentes,
            "bacterias muertas": bacterias_muertas,
            "biofilm": biofilm
        }

    def exportar_csv(self, estados_grilla):
        estados = [["bacterias vivas", "bacterias resistentes", "bacterias muertas", "biofilm"]]
        for grilla in estados_grilla[1:]:
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
            estado = self.reporte_estado(grilla)
            print(estado)

        with open('data_bacterias.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(estados)
