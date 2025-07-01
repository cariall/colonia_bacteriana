import random
import csv
from bacteria import Bacteria
from colonia import Colonia
import matplotlib.pyplot as plt

class Simulador():
    def __init__(self, grilla, cax, textos):
        self.__grilla = grilla
        self.__estados_grilla = [grilla]
        self.__cax = cax
        self.__textos = textos

        self.__colonia= Colonia()

    def inicializar_bacterias(self):
        interactores = [0, 0, 4, 1, 0, 0, 0, 0, 0, 3]
        
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

                # print(f"en {i, j} hay número {item}")
        self.__colonia.exportar_csv(self.__estados_grilla)
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
                          
        self.__grilla = self.__colonia.modificar_ambiente(self.__grilla) 
        for i in range(len(self.__grilla)):
            for j in range(len(self.__grilla[0])):
                val = self.__grilla[i][j]
                self.__textos[i][j].set_text(str(int(val)) if val > 0 else '')
        self.__estados_grilla.append(self.__grilla.copy()) 
        self.__colonia.exportar_csv(self.__estados_grilla)
        self.__cax.set_data(self.__grilla.copy())

        print("Grilla actual")
        for fila in self.__grilla:
            print(fila) 
            
        return [self.__cax] + [t for fila in self.__textos for t in fila]

    def graficar_crecimiento_resistencia(nombre_archivo, columna, nombre_y, titulo):
        datos = []
        with open(nombre_archivo, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Salta la cabecera
            for row in reader:
                datos.append(int(row[columna]))
        fig, ax = plt.subplots() #Crea figura y ejes vs plt.figure que sólo crea la figura sin ejes.
        fig.canvas.manager.set_window_title("Gráfico de evolución")  #Para título de ventana
        plt.plot(datos, marker='o')
        plt.xlabel('Paso')
        plt.ylabel(nombre_y)
        plt.title(titulo)
        plt.show()
                            

