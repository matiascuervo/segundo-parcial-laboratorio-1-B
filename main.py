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
#from formularios.gestion_formularios import Gestion_formulario
from formularios.gestion_formularios import*


pygame.init()
#PANTALLA///////////////////////////////////////////
W,H = 1200,600
TAMAÑO_PANTALLA= (W,H)

FPS = 15

clock = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))

fondo_pantalla = pygame.image.load("./mapa/mapa_1.jpg")
fondo_escalado = pygame.transform.scale(fondo_pantalla, TAMAÑO_PANTALLA)

COLOR_NEGRO = (0, 0, 0)
COLOR_FONDO = COLOR_NEGRO
#PANTALLA///////////////////////////////////////////
#imagen_corazon = personaje.cargar_sprites_corazones()
#mirando_izquierda = False

  
#PERSONAJE//////////////////////////////////////



#////////////////


#pygame.mixer.music.load("juego_parcial\Arrow_Hit_DamageAdd_WeakHit.wav")
#PISO//////////////////
  # Ajusta la altura de la planta según tus necesidades
#proyctiles///////////



gestinador_formularios = Gestion_formulario(PANTALLA)

nivelActivo = "nivel1"


while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
    
    teclas = pygame.key.get_pressed()
    gestinador_formularios.gestionar_formulario(teclas,[evento])
    
               
    
    #mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(f"Coordenadas del cursor del mouse: ({mouse_x}, {mouse_y})")
    """if get_mode() == True:
        pygame.draw.rect(PANTALLA,"BLUE", personaje.rectangulo_personaje,2)
       # pygame.draw.rect(PANTALLA,"RED", miNivel.piso,2)
        pygame.draw.rect(PANTALLA,"RED",plataforma.rectangulo_plataforma,2)
        pygame.draw.rect(PANTALLA,"RED",plataforma_2.rectangulo_plataforma,2)
        pygame.draw.rect(PANTALLA,"RED",plataforma_3.rectangulo_plataforma,2)
        pygame.draw.rect(PANTALLA, (0, 0, 255), plataforma.obtener_rectangulos()["bottom"], 2)
        pygame.draw.rect(PANTALLA, (0, 0, 0), personaje.obtener_rectangulos()["left"], 2)
        pygame.draw.rect(PANTALLA,"RED",gusano_enemigo.rectangulo_enemigo,2)
        pygame.draw.rect(PANTALLA,"RED",planta_enemigo.rectangulo_enemigo,2)
        for proyectil in lista_proyectiles:
             pygame.draw.rect(PANTALLA, (255, 0, 0), proyectil.rect, 2)
        for proyectil in planta_enemigo.lista_proyectiles_enemigo:
               pygame.draw.rect(PANTALLA, (255, 100, 0), proyectil.rect, 2)"""
        
            

      

   
    pygame.display.update()     
    #pygame.time.delay(50)

    
