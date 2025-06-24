import random
from bacteria import Bacteria

class Colonia():
    def __init__(self):
        self.__lista_bacterias = []
        #self.__ambiente = Ambiente()
        self.__biofilm = []

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
        print(bacteria.obtener_datos())
        self.__lista_bacterias.append(bacteria)

    def paso(self, grilla):
        print(f"bacterias: {len(self.__lista_bacterias)}")  
        bacterias_antiguas = self.__lista_bacterias
        energia_mitosis = 50

        for bacteria in bacterias_antiguas:
            # nuevos_estados = [1, 2, 3]
            # nuevo_estado = random.choice(nuevos_estados)
            # bacteria.set_estado(nuevo_estado) 
            x,y  = bacteria.get_id()
            energia_actual = bacteria.get_energia()

            if bacteria.get_estado() == 1:
                grilla[x][y] = 1

            if bacteria.get_estado() == 2:
                grilla[x][y] = 2

            grilla[x][y] = bacteria.get_estado()
            # print(f"coordenadas bacteria: {x, y}")     
            # print(f"estado bacteria: {bacteria.get_estado()}") 
            
            vecinos = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
            for nx, ny in vecinos:
                if 0 <= nx < len(grilla) and 0 <= ny < len(grilla[0]):
                    if grilla[nx][ny] == 4:
                        print(f"Bacteria detecta en {(x, y)} biofilm en {(nx, ny)}")
                        bacteria.alimentar(15)
                        print(f"energía actual bacteria: {bacteria.get_energia()}")
                        if energia_actual >= energia_mitosis:
                            bacteria.dividirse()
            else:
                energia_sin_comer = bacteria.set_energia(energia_actual - 10)
                print(f"energía después de no consumir nutrientes {energia_sin_comer}")
                if energia_actual == 0:
                    nueva_bacteria_muerta= bacteria.set_estado(2)
                    print(f"bacteria sin energía pasa a estar muerta {nueva_bacteria_muerta}")

        print("--------------------------Paso siguiente--------------------------")
        # print("Paso 1: 20 bacterias activas colonizan aleatoriamente la placa. Todas comienzan con energía = 50. No hay divisiones ni muertes.")
        # print("Paso 2: 18 bacterias mueren al ingresar a zona con antibiótico. 2 mueren por falta de nutrientes")
        # print("Paso 3: 3 bacterias mueren al ingresar a zona con antibiótico. Una muta y se vuelve resistente")
        # print("Paso 4: 5 nuevas mutaciones; 3 efectivas. 20 divisiones. Empieza la escasez de nutrientes")
        # print("Paso 5: 6 muertes por inanición. La zona central es dominada por bacterias resistentes.")
        print("------------------------------------------------------------------")

        print("Grilla actual")
        for fila in grilla:
            print(fila)

        print(f"coordenadas bacteria: {x, y}")     
        print(f"estado bacteria: {bacteria.get_estado()}")

        if grilla[x][y] != bacteria.get_estado():
            print(f"¡Desincronización! En ({x},{y}) grilla={grilla[x][y]}, bacteria={bacteria.get_estado()}")
        # Implementamos logica para actualizar un paso en la colonia
        # donde cada bacteria tendrá un mo vimiento aleatorio y dependiendo de lo que 
        # encuentre, podrá morir, mutar o dividirse, comer biofilm.
        return bacterias_antiguas
        
    def reporte_estado():
        pass

    def exportar_csv():
        pass
