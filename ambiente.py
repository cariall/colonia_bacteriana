import random
import numpy as np

class Ambiente:
    def __init__(self, ancho, alto, nutrientes_inicial=100, factor_inicial = 0):
        self.__nutrientes = np.full((ancho, alto), nutrientes_inicial, dtype=int) #crea matriz de nutrientes
        self.__factor_ambiental = np.full((ancho, alto), factor_inicial, dtype=int) #crea matriz de factor ambiental
    
    def difundir_nutrientes(self, tasa=0.1):
        nutrientes_nueva = self.__nutrientes
        for i in range(1, self.__nutrientes.shape[0] - 1):
            for j in range(1, self.__nutrientes.shape[1] - 1): #reemplaza len(self.nutrientes)
                vecinos = self.__nutrientes[i-1:i+2, j-1:j+2]  #inicio:fin
                nutrientes_nueva[i, j] += tasa * (vecinos.mean() - self.__nutrientes[i, j]) #mean calcula el promedio de los nutrientes
        self.__nutrientes = nutrientes_nueva
        
    def consumir_nutriente(self, x, y, cantidad):
        self.__nutrientes[x, y] = max(0, self.__nutrientes[x, y] - cantidad)

    def actualizar_nutrientes(self, grilla):
        ancho = len(grilla)
        alto = len(grilla[0])
        movimientos = [(-1,0), (1,0), (0,-1), (0,1)]  

        nuevas_posiciones = []

        for i in range(ancho):
            for j in range(alto):
                if grilla[i][j] == 4: #si encuentra biofilm
                    random.shuffle(movimientos) #un random de la lista
                    for dx, dy in movimientos: #coordenada
                        ni, nj = i + dx, j + dy #se mueve coordenada desde donde está más número al azar de movimientos 
                        if 0 <= ni < ancho and 0 <= nj < alto and grilla[ni][nj] == 0: #si el espacio está vacío, agrega biofilm en nueva posición
                            nuevas_posiciones.append(((i, j), (ni, nj)))
                            break

        for (i, j), (ni, nj) in nuevas_posiciones: #deja donde estaba biofilm en blanco y el nuevo espacio con biofilm
            grilla[ni][nj] = 4
            grilla[i][j] = 0
        return grilla

    def aplicar_factor_ambiental(self, grilla):
        ancho = len(grilla)
        alto = len(grilla[0])
        for i in range(ancho):
            for j in range(alto):
                # Si hay antibiótico en esta celda
                if grilla[i][j] == 5:
                    # Revisa las 4 celdas vecinas
                    vecinos = [(-1,0), (1,0), (0,-1), (0,1)]
                    for dx, dy in vecinos:
                        ni, nj = i + dx, j + dy 
                        if 0 <= ni < ancho and 0 <= nj < alto:
                            # Si hay bacteria activa (1), la mata (2)
                            if grilla[ni][nj] == 1:
                                print(f"Antibiótico en {i, j} mató a la bacteria en {ni, nj}")
                                grilla[ni][nj] = 2
        return grilla

    def aplicar_ambiente(self, grilla):
        self.difundir_nutrientes()
        grilla = self.actualizar_nutrientes(grilla)
        grilla = self.aplicar_factor_ambiental(grilla)
        return grilla
    
    
    
   