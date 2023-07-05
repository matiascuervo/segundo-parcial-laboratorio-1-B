import pygame
import sys
from pygame.locals import* 
from formulario_carga import Formulario_main
from gestion_formularios import Gestion_formulario

pygame.init()

WIDTH = 1200
HEIGHT = 600
FPS = 60

RELOG =pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
fondo_pantalla = pygame.image.load("formularios\cosas_formularios/fondo_formulario.png")
fondo_escalado = pygame.transform.scale(fondo_pantalla, (WIDTH,HEIGHT))
from_prueba = Formulario_main(pantalla, 200, 20, 900, 550, "formularios\cosas_formularios/tabla_score.png", "White", 3, True)
gestinador_formularios =Gestion_formulario(pantalla)



while True:
    RELOG.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        teclas = pygame.key.get_pressed()
        pantalla.fill("black")
        pantalla.blit(fondo_escalado, (0,0))
        gestinador_formularios.gestionar_formulario(teclas,[evento])


    #mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(f"Coordenadas del cursor del mouse: ({mouse_x}, {mouse_y})")      
    
    pygame.display.flip()
  