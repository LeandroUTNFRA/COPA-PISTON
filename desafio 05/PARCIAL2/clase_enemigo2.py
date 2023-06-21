import pygame
import random
from clase_enemigo import Enemigo

class Enemigo2(Enemigo):

    def __init__(self, x, y, imagen_path, tamanio) -> None:
        super().__init__(x, y, imagen_path, tamanio)  