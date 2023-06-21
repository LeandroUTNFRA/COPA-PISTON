import pygame
from pygame.locals import*
import random

class Auto:
    def __init__(self, x, y, imagen_path, width, height):
        self.imagen_original = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen_original, (width, height))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.vida=100
        self.controles_cambiados = True
        self.duracion_cambio_controles = 3000  # 3 segundos de duración para el cambio de controles
        self.tiempo_movimientos_aleatorios = 0
    
    def mover(self, direccion):
        if self.controles_cambiados:
            if direccion == "izquierda":
                self.rect.x -= self.speed
            elif direccion == "derecha":
                self.rect.x += self.speed
            elif direccion == "arriba":
                self.rect.y -= self.speed
            elif direccion == "abajo":
                self.rect.y += self.speed
        else:
            if pygame.time.get_ticks() - self.tiempo_movimientos_aleatorios < self.duracion_cambio_controles:
                # Realizar movimientos aleatorios de derecha a izquierda
                if random.random() < 0.5:
                    self.rect.x -= self.speed
                else:
                    self.rect.x += self.speed
            else:
                self.controles_cambiados = True

        if self.rect.left < 200:
            self.rect.left = 200

        if self.rect.right > 1000:
            self.rect.right = 1000

        if self.rect.bottom > 600:
            self.rect.bottom = 600

        if self.rect.top < 0:
            self.rect.top = 0

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
