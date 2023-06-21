import pygame
from pygame.locals import*
import sys
import sqlite3

def guardar_puntuacion(nombre_jugador, puntuacion):
    conn = sqlite3.connect("ranking.db")
    #Se crea un objeto cursor que se utiliza para ejecutar comandos SQL en la base de datos.
    cursor = conn.cursor()
    #Esta línea ejecuta una sentencia SQL para crear una tabla llamada "ranking" en la base de datos, si no existe.
    cursor.execute("CREATE TABLE IF NOT EXISTS ranking (nombre TEXT, puntuacion INTEGER)")
    cursor.execute("INSERT INTO ranking (nombre, puntuacion) VALUES (?, ?)", (nombre_jugador, puntuacion))
    conn.commit()
    conn.close()

def mostrar_ranking(pantalla):
    conn = sqlite3.connect("ranking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, puntuacion FROM ranking ORDER BY puntuacion DESC")
    #obtiene todas las filas seleccionadas por la consulta SQL y 
    #las almacena en la variable ranking. Cada fila se representa como una tupla
    ranking = cursor.fetchall()
    conn.close()

    # Mostrar el ranking en la pantalla del juego
    font=pygame.font.SysFont("Anton",36)
    y_pos =260  # Posición inicial en Y para mostrar los nombres del ranking

    for i, (nombre, puntuacion) in enumerate(ranking):
        texto_ranking = font.render(f"{i+1}. {nombre}: {puntuacion}", True, (0, 0, 0))
        pantalla.blit(texto_ranking, (10, y_pos))
        y_pos += 30

def esperar_tecla():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return event.key

def mostrar_ranking_y_esperar(pantalla):
    pantalla.fill((0, 0, 0))
    imagen_final=pygame.image.load("D:\\archivos\\desafio 05\\IMG\\WhatsApp Image 2023-06-20 at 11.41.55.jpeg")
    imagen_final = pygame.transform.scale(imagen_final, (1200,600))
    pantalla.blit(imagen_final, (0, 0))
    mostrar_ranking(pantalla)
    pygame.display.flip()

    # Esperar a que se presione Enter para jugar de nuevo o salir
    
    font = pygame.font.Font(None, 36)
    texto_mensaje = font.render("Presiona Enter para jugar de nuevo", True, (0, 0, 0))
    pantalla.blit(texto_mensaje, (1200/2 - texto_mensaje.get_width()/2, 600/2 - texto_mensaje.get_height()/2))
    pygame.display.flip()

    tecla = esperar_tecla()
    if tecla == K_RETURN:
        return True  # Volver a jugar
    else:
        pygame.quit()
        sys.exit()


def mostrar_menu(pantalla):
    menu_surface = pygame.Surface((1200, 600))
    menu_surface.fill((0, 0, 0))  # Color de fondo del menú

    #para almacenar el nombre ingresado por el usuario.
    nombre_jugador = ""

    font = pygame.font.Font(None, 36)
    titulo = font.render("¡Bienvenido a la Copa Pistón!", True, (0, 0, 0))
    instrucciones = font.render("Ingresa tu nombre y presiona Enter para comenzar", True, (0, 0, 0))
    nombre_etiqueta = font.render("Nombre: ", True, (0, 0, 0))

    #imagen
    imagen_logo = pygame.image.load("D:\\archivos\\desafio 05\\IMG\\menu_principal.jpg")
    imagen_logo = pygame.transform.scale(imagen_logo, (1200,600))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                #al presionar la tecla "Enter", devuelve el nombre ingresado y salir del bucle while, permitiendo 
                # que el programa continúe con el flujo de ejecución posterior al llamado de la función.
                if event.key == K_RETURN:
                    return nombre_jugador  # Devuelve el nombre ingresado

                elif event.key == K_BACKSPACE:
                    nombre_jugador = nombre_jugador[:-1]  # Elimina el último carácter del nombre

                else:
                    nombre_jugador += event.unicode  # Agrega el carácter ingresado al nombre


        

        menu_surface.fill((0, 0, 0))  # Vuelve a llenar el fondo del menú en cada iteración
        menu_surface.blit(imagen_logo, (0, 0))
        menu_surface.blit(titulo, (10, 90))
        menu_surface.blit(instrucciones, (10, 130))
        menu_surface.blit(nombre_etiqueta, (10, 200))

        # Renderizar el nombre del jugador actualizado
        nombre_texto = font.render(nombre_jugador, True, (0, 0, 0))
        menu_surface.blit(nombre_texto, (120, 200))

        

        pantalla.blit(menu_surface, (0, 0))
        pygame.display.flip()
