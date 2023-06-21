import pygame

def mover_fondo(pantalla, alto_pantalla, imagen_pista, y):
    y_relativa = y % imagen_pista.get_rect().height
    # esta línea dibuja el fondo de la pista en la pantalla, justo arriba de la posición 
    # actual del fondo, permitiendo el desplazamiento continuo del fondo hacia arriba.
    pantalla.blit(imagen_pista, (0, y_relativa - imagen_pista.get_rect().height))
    if y_relativa < alto_pantalla:
        pantalla.blit(imagen_pista, (0, y_relativa))
    y -= 1
    return y

def barra_de_vida(pantalla,x,y,vida,auto):
    largo=200
    ancho=25
    #esto es un calculo que por ejemplo me saco 5 de vida se va representar un 5% de la barra
    calculo=int((auto.vida/100)*largo)
    #especificamos el borde y el rectangulo
    borde=pygame.Rect(x,y,largo,ancho)
    rectangulo= pygame.Rect(x,y,calculo,ancho)
    #aca dibujamos
    pygame.draw.rect(pantalla,"Blue",borde,3)#3 el grosor del  borde
    pygame.draw.rect(pantalla,"Red",rectangulo)
    imagen_barra_vida = pygame.image.load("D:\\archivos\\desafio 05\\IMG\\Mi proyecto 123.png")
    imagen_advertencia= pygame.image.load("D:\\archivos\\desafio 05\\IMG\\Mi proyecto (3).png")
    pantalla.blit(pygame.transform.scale(imagen_barra_vida,(25,25)),(450,15))
    if auto.vida<0:
        #esto es para que la barra no se valla de lugar 
        auto.vida=0
    if auto.vida<30:
        pantalla.blit(pygame.transform.scale(imagen_advertencia,(25,25)),(450,15))