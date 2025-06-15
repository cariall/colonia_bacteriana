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
    # Crear un mapa de colores con 5 categor ´ıas (0 = vac´ıo)
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

    # Configuraci ´on de la grilla
    ax.set_xticks(np.arange(0, 10, 1))
    ax.set_yticks(np.arange(0, 10, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color='gray', linestyle='-', linewidth=0.5)

    # Mostrar valores en cada celda
    for i in range(10):
        for j in range(10) :
            val = grilla[i, j]
            if val > 0:
                ax.text(j, i, int(val), va='center', ha='center', color ='white')


    sim = Simulador(grilla, cax)
    plt.title("Grilla bacteriana (10 x10)")
    plt.tight_layout()
    anim = FuncAnimation(fig, sim.run, blit=False, interval=500, save_count=100, frames=5, repeat=False)
    plt.show()