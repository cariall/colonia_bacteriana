import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import random
from matplotlib.animation import FuncAnimation
from simulador import Simulador
from matplotlib.widgets import Button #para poder integrar botones

ANCHO_GRILLA = 10
ALTO_GRILLA = 10
# Crear una grilla 10 x10
grilla = np.zeros((ANCHO_GRILLA, ALTO_GRILLA))
interactores = [0, 0, 0, 0, 1, 0, 4, 0, 5, 3]
# Definimos posiciones de bacterias activas (1) , muertas (2) , resistentes
# (3) , biofilm (4)

def iniciar():
    for i in range(ANCHO_GRILLA):
        for j in range(ALTO_GRILLA):
            item = random.choice(interactores)
            if item != 0:
                grilla[i, j] = item 
    # Crear un mapa de colores con 5 categorías (0 = vacío)
    cmap = plt.cm.get_cmap('Set1',6)

    fig, ax = plt.subplots(figsize=(10, 12)) #porte de la ventana
    cax = ax.matshow(grilla, cmap=cmap)

    # Agrega leyenda personalizada
    legend_elements = [
        Patch(facecolor=cmap(1/6), label='Bacteria activa'),
        Patch(facecolor=cmap(2/6), label='Bacteria muerta'),
        Patch(facecolor=cmap(3/6), label='Bacteria resistente'),
        Patch(facecolor=cmap(4/6), label='Biofilm'),
        Patch(facecolor=cmap(5/6), label='Antibiótico'),
    ]

    ax.legend(handles=legend_elements, loc ='upper right', bbox_to_anchor=(1.45, 1))

    #---Agrego un botón---
    plt.subplots_adjust(bottom=0.2)  # deja espacio para el botón
    ax_boton = plt.axes([0.25, 0.05, 0.2, 0.075]) #posición horizontal, posición vertical, ancho y alto.
    boton = Button(ax_boton, 'Graficar Resistencia')

    def on_boton_clicked(event):
        Simulador.graficar_crecimiento_resistencia(
            'data_bacterias.csv',
            columna=1,
            nombre_y='Bacterias resistentes',
            titulo='Evolución de bacterias resistentes'
        )
    boton.on_clicked(on_boton_clicked)

    #---Agrego botón de crecimiento---
    ax_boton_crec = plt.axes([0.55, 0.05, 0.2, 0.075]) #posición
    boton_crec = Button(ax_boton_crec, 'Graficar Crecimiento')

    def on_boton_crec_clicked(event):
        Simulador.graficar_crecimiento_resistencia(
            'data_bacterias.csv',
            columna=0,
            nombre_y='Bacterias vivas',
            titulo='Crecimiento de bacterias vivas'
        )
    boton_crec.on_clicked(on_boton_crec_clicked)

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
    fig.suptitle("Grilla bacteriana (10 x10)", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # deja espacio arriba para el título
    sim.inicializar_bacterias()
 
    anim = FuncAnimation(fig, sim.run, blit=False, interval=3000, save_count=4, frames=3, repeat=False)
    plt.show()