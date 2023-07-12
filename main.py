import pygame
import sys
import random
from animaciones import*
from pygame.locals import*
from modo_programador import*
from proyectiles import*
from personaje import Personaje
from plataforma import Plataforma
from enemigo import Enemigo
from planta_enemigo import PlantaEnemigo
from animacion_enemigo import*
from proyectil_enemigo import *
from itemYvida import Item
from clase_nivel import Nivel
from formularios.gestion_formularios import*

#from formularios.gestion_formularios import Gestion_formulario


pygame.init()
#PANTALLA///////////////////////////////////////////
W,H = 1000,600
TAMAÑO_PANTALLA= (W,H)

FPS = 15

clock = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))

#fondo_pantalla = pygame.image.load("./mapa/mapa_1.jpg")
#fondo_escalado = pygame.transform.scale(fondo_pantalla, TAMAÑO_PANTALLA)

COLOR_NEGRO = (0, 0, 0)
COLOR_FONDO = COLOR_NEGRO

gestinador_formularios = Gestion_formulario(PANTALLA)


#nivelActivo = "nivel1"


while True:
    try:
        clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()

        teclas = pygame.key.get_pressed()
        gestinador_formularios.gestionar_formulario(teclas, [evento])

        pygame.display.update()

    except Exception as e:
        # Manejo de la excepción
        print("Se produjo un error:", str(e),"Contacte al Soporte Para Mas Ayuda")

    
    #mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(f"Coordenadas del cursor del mouse: ({mouse_x}, {mouse_y})")
    
            

      

    #pygame.time.delay(50)

    
