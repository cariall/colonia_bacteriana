from colonia import Colonia
from bacteria import Bacteria

def iniciar(self):
    Colonia.agregar_bacteria(self)
    instancia = Colonia()
    instancia.alimentar()

if __name__ == "__main__":
    iniciar()