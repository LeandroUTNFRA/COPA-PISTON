import pygame
import random
#from clase_controles import Controles

class Charco:
    def __init__(self,x,y,imagen_path,tamanio) -> None:
        self.imagen_original = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen_original, (tamanio))
        self.charco_rect = self.imagen.get_rect()
        self.charco_rect.x = x
        self.charco_rect.y = y
        self.speed = random.randrange(1,6)

    def generar_charcos(cantidad,imagen):
        lista_charcos = []
        for i in range(cantidad):
            #x = random.randrange(0, 1200)
            y = random.randrange(-600, 0)
            auto = Charco(0+(i*50), y, imagen, (100, 100))
            lista_charcos.append(auto)

        return lista_charcos

    def movimiento(self,alto_pantalla):
        self.charco_rect.y += self.speed
        if self.charco_rect.top > alto_pantalla:
            self.charco_rect.x= random.randrange(0,600)
            self.charco_rect.y= -100
            
        elif self.charco_rect.bottom < 0:
            self.charco_rect.top = alto_pantalla   
        
        if self.charco_rect.left <200:
            self.charco_rect.left = 200
            

        if self.charco_rect.right> 1000:
            self.charco_rect.right=1000
            
        

    def update(self,pantalla):
        self.movimiento(pantalla.get_height())
        pantalla.blit(self.imagen, self.charco_rect)
            