import pygame
import random

class Enemigo:
    def __init__(self,x,y,imagen_path,tamanio) -> None:
        
        self.imagen_original = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen_original, (tamanio))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randrange(1,7)
        self.direccion = random.choice([-1, 1])  # -1 para moverse hacia la izquierda, 1 para moverse hacia la derecha

    def generar_autos(cantidad,imagen):
        lista_autos = []
        for i in range(cantidad):
            #x = random.randrange(0, 1200)
            y = random.randrange(-600, 0)
            auto = Enemigo(0+(i*50), y, imagen, (100, 100))
            lista_autos.append(auto)

        return lista_autos

    def mover_y(self,alto_pantalla):
        self.rect.y += self.speed
        if self.rect.top > alto_pantalla:
            self.rect.x= random.randrange(0,600)
            self.rect.y= -100
            self.direccion = random.choice([-1, 1])

        elif self.rect.bottom < 0:
            self.rect.top = alto_pantalla   
        
        if self.rect.left <200:
            self.rect.left = 200
            self.direccion = 1  # Cambiar la dirección a derecha si llega al límite izquierdo

        if self.rect.right> 1000:
            self.rect.right=1000
            self.direccion = -1  # Cambiar la dirección a izquierda si llega al límite derecho

        #esta línea de código controla el movimiento horizontal del enemigo en la 
        # dirección especificada por self.direccion y con la velocidad determinada por self.speed.
        self.rect.x += self.speed * self.direccion  # Mover en la dirección actual

    def update(self,pantalla):
        self.mover_y(pantalla.get_height())
        pantalla.blit(self.imagen, self.rect)
            