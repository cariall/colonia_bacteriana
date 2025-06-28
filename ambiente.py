import random

class Ambiente:
    def __init__(self):
        pass

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

    def aplicar_ambiente(self, grilla):
        self.actualizar_nutrientes(grilla)
        return grilla
    