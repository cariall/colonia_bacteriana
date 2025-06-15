from bacteria import Bacteria

class Colonia():
    def __init__(self, bacterias):
        self.bacterias = bacterias
        #self.__ambiente = Ambiente()

    def agregar_bacteria(self):
        bacteria1 = Bacteria("X2M4AF", "Escherichia coli K-12", 87, True, "activa")
        bacteria2 = Bacteria("P3N9WQ", "Bacillus subtilis 168", 42, False, "latente")
        bacteria3 = Bacteria("Z8L1KD", "Staphylococcus aureus USA300", 95, True, "activa")
        self.bacterias = [bacteria1, bacteria2, bacteria3]
        return self.bacterias

    def paso():
        print("Paso 1: 20 bacterias activas colonizan aleatoriamente la placa. Todas comienzan con energía = 50. No hay divisiones ni muertes.")
        print("Paso 2: 18 bacterias mueren al ingresar a zona con antibiótico. 2 mueren por falta de nutrientes")
        print("Paso 3: 3 bacterias mueren al ingresar a zona con antibiótico. Una muta y se vuelve resistente")
        print("Paso 4: 5 nuevas mutaciones; 3 efectivas. 20 divisiones. Empieza la escasez de nutrientes")
        print("Paso 5: 6 muertes por inanición. La zona central es dominada por bacterias resistentes.")

    def reporte_estado():
        pass

    def exportar_csv():
        pass
