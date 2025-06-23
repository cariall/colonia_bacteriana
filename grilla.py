import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import random
from matplotlib.animation import FuncAnimation
from simulador import Simulador

ANCHO_GRILLA = 10
ALTO_GRILLA = 10
# Crear una grilla 10 x10
grilla = np.zeros((ANCHO_GRILLA, ALTO_GRILLA))
interactores = [0, 0, 0, 4, 1, 1, 4, 3, 1, 3]
# Definimos posiciones de bacterias activas (1) , muertas (2) , resistentes
# (3) , biofilm (4)

def iniciar():
    for i in range(ANCHO_GRILLA):
        for j in range(ALTO_GRILLA):
            item = random.choice(interactores)
            if item != 0:
                grilla[i, j] = item 
    # Crear un mapa de colores con 5 categorías (0 = vacío)
    cmap = plt.cm.get_cmap('Set1',5)

    fig, ax = plt.subplots(figsize=(6, 6))
    cax = ax.matshow(grilla, cmap=cmap)

    # Agrega leyenda personalizada
    legend_elements = [
        Patch(facecolor=cmap(1/5), label='Bacteria activa'),
        Patch(facecolor=cmap(2/5), label='Bacteria muerta'),
        Patch(facecolor=cmap(3/5), label='Bacteria resistente'),
        Patch(facecolor=cmap(4/5), label='Biofilm'),
    ]

    ax.legend(handles=legend_elements, loc ='upper right', bbox_to_anchor=(1.45, 1) )

    # Configuración de la grilla
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color='gray', linestyle='-', linewidth=0.5)

    textos = []
    for i in range(ANCHO_GRILLA):
        fila = []
        for j in range(ALTO_GRILLA):
            val = grilla[i, j]
            t = ax.text(j, i, int(val) if val > 0 else '', va='center', ha='center', color='white')
            fila.append(t)
        textos.append(fila)

    sim = Simulador(grilla, cax, textos)
    plt.title("Grilla bacteriana (10 x10)")
    plt.tight_layout()
    sim.inicializar_bacterias()
    anim = FuncAnimation(fig, sim.run, blit=False, interval=2000, save_count=100, frames=4, repeat=False)
    plt.show()