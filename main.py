import grilla
from simulador import Simulador

simulador = Simulador(None, None, None)

def iniciar():
    grilla.iniciar()

if __name__ == "__main__":
    iniciar()
    simulador.graficar_columna_csv('data_bacterias.csv', 1, 'Bacterias resistentes', 'Evolución de bacterias resistentes')