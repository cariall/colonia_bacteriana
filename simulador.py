import random

class Simulador():
    def __init__(self, grilla, cax):
        self.__grilla = grilla
        self.__cax = cax

    def run(self, frame):
        interactores = [0, 0, 0, 4, 1, 1, 4, 3, 1, 3]
        for i in range(len(self.__grilla)):
            for j in range(len(self.__grilla[i])):
                item = random.choice(interactores)
                if item != 0:
                    self.__grilla[i, j] = item 
        self.__cax.set_data(self.__grilla)
        return [self.__cax]

