import pygame
from pygame.locals import*
import sys
from clase_auto import Auto
from clase_enemigo import Enemigo
from clase_enemigo2 import Enemigo2
from menu import *
from clase_charco import Charco
import random
from funciones import*

pygame.init()
 
#fps
RELOJ = pygame.time.Clock()
FPS= 60

#pantalla
ANCHO= 1200
ALTO= 600
y=0

#IMAGEN FONDO
imagen_pista= pygame.image.load("D:\\archivos\\desafio 05\\IMG\\PISTA1.jpg")
imagen_pista= pygame.transform.scale(imagen_pista,(ANCHO,ALTO))

#TITULO y TAMAÑO DE PANTALLA
pygame.display.set_caption("LA COPA PISTON")
pantalla= pygame.display.set_mode((ANCHO,ALTO))

#PERSONAJES
lista_autos= Enemigo.generar_autos(2,"D:\\archivos\\desafio 05\\IMG\\Mi proyecto (2).png")
lista_autos2=Enemigo2.generar_autos(2,"D:\\archivos\\desafio 05\\IMG\\auto Driño celeste.png")
lista_charcos=Charco.generar_charcos(1,"D:\\archivos\\desafio 05\\IMG\\Mi proyecto (4)3.png")
auto = Auto(ANCHO/2, ALTO/2, "D:\\archivos\\desafio 05\\IMG\Mi proyecto 123.png",100,100)

#MUSICA DE FONDO
musica=pygame.mixer.Sound("D:\\archivos\\desafio 05\\Parcial Labo 2\\Cars Life is a highway.mp3")
pygame.mixer.Sound.play(musica,-1)
musica.set_volume(1)

#SONIDO DE MOVIMIENTO
sonido_movimiento=pygame.mixer.Sound("D:\\archivos\\desafio 05\\Parcial Labo 2\\Cars 1, 2 y 3 - Efectos de Sonido (HD) (1) (1).mp3")
sonido_movimiento.set_volume(0.1)

#SCORE 
puntuacion = 0  # Variable para almacenar la puntuación
tiempo_incremento = 1000  # Intervalo de tiempo en milisegundos para incrementar la puntuación
tiempo_acumulado = 0  # Variable para llevar el control del tiempo acumulado

#MENU DE INICIO
nombre_jugador = mostrar_menu(pantalla)

while True:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    if auto.controles_cambiados== True:
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            auto.mover("izquierda")
            pygame.mixer.Sound.play(sonido_movimiento)
        if keys[K_RIGHT]:
            auto.mover("derecha")
            pygame.mixer.Sound.play(sonido_movimiento)
        if keys[K_UP]:
            auto.mover("arriba")
            pygame.mixer.Sound.play(sonido_movimiento)
        if keys[K_DOWN]:
            auto.mover("abajo")
            pygame.mixer.Sound.play(sonido_movimiento)
    else:
        if pygame.time.get_ticks() - auto.tiempo_movimientos_aleatorios < auto.duracion_cambio_controles :
            if random.random() < 0.5:
                auto.mover("izquierda")
            else:
                auto.mover("derecha")
        else:
            auto.controles_cambiados = True
        
    #En este caso, la función mover_fondo recibe y como un parámetro adicional. 
    # Después de actualizar el valor de y, se devuelve el nuevo valor y se asigna 
    # nuevamente a la variable y en el bucle principal del juego.
    y = mover_fondo(pantalla, ALTO, imagen_pista, y)

    tiempo_acumulado += RELOJ.get_time()
    if tiempo_acumulado >= tiempo_incremento:
        puntuacion += 1
        tiempo_acumulado = 0

    auto.dibujar(pantalla)
    
    barra_de_vida(pantalla,500,15,auto.vida,auto)

    for enemigo in lista_autos:
        enemigo.update(pantalla)
        if auto.rect.colliderect(enemigo.rect): 
            auto.vida-=5
            enemigo.rect.y= -200
            puntuacion-=2
    for enemigo2 in lista_autos2:
        enemigo2.update(pantalla)
        if auto.rect.colliderect(enemigo2.rect): 
            auto.vida-=10
            enemigo2.rect.y= -200
            puntuacion-=3
    for charco in lista_charcos:
        charco.update(pantalla)
        if auto.rect.colliderect(charco.charco_rect):
            charco.charco_rect.y=-200
            auto.controles_cambiados = False
            auto.tiempo_movimientos_aleatorios = pygame.time.get_ticks()
        
    #for enemigo,enemigo2,charco in zip(lista_autos,lista_autos2,lista_charcos):
    font = pygame.font.Font(None, 36)
    texto_puntuacion = font.render("Puntuación: " + str(puntuacion), True, (255, 255, 255))
    pantalla.blit(texto_puntuacion, (10, 10))

    #caundo la vida del auto sea menor a 0 muestra el ranking de puntos 
    #y le pregunta si quiere volver a jugar
    if auto.vida<0:
        guardar_puntuacion(nombre_jugador,puntuacion)
        if mostrar_ranking_y_esperar(pantalla):
            # Reiniciar el juego
            nombre_jugador = mostrar_menu(pantalla)
            auto = Auto(ANCHO/2, ALTO/2, "D:\\archivos\\desafio 05\\IMG\\Mi proyecto 123.png",100,100)
            puntuacion = 0
        else:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()

