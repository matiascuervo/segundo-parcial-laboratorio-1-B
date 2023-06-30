import pygame
from animaciones import*

gusano = [
    pygame.image.load("juego_parcial\enemigos\gusanito/0.png"),
    pygame.image.load("juego_parcial\enemigos\gusanito/1.png"),
    pygame.image.load("juego_parcial\enemigos\gusanito/2.png"),
    pygame.image.load("juego_parcial\enemigos\gusanito/3.png")
]

gusano_izquierda=[
    pygame.image.load("juego_parcial\enemigos\gusanito/4.png"),
    pygame.image.load("juego_parcial\enemigos\gusanito/5.png"),
    pygame.image.load("juego_parcial\enemigos\gusanito/6.png"),
    pygame.image.load("juego_parcial\enemigos\gusanito/7.png")]

gusano_muerto =girar_imagenes(gusano,False,True)

troll=[pygame.image.load("juego_parcial\enemigos/troll/22.png"),
       pygame.image.load("juego_parcial\enemigos/troll/23.png"),
       pygame.image.load("juego_parcial\enemigos/troll/24.png"),
       pygame.image.load("juego_parcial\enemigos/troll/troll_daño.png")]


planta=[pygame.image.load("juego_parcial\enemigos\planta/17.png"),
        pygame.image.load("juego_parcial\enemigos\planta/18.png"),
        pygame.image.load("juego_parcial\enemigos\planta/19.png"),
        pygame.image.load("juego_parcial\enemigos\planta/20.png")]
planta_izquierda =girar_imagenes(planta,True,False)
lista_animaciones_planta = [planta,planta_izquierda]
boss=[pygame.image.load("juego_parcial\enemigos/boss/boss_0.png"),
      pygame.image.load("juego_parcial\enemigos/boss/boss_1.png"),
      pygame.image.load("juego_parcial\enemigos/boss/boss_2.png"),
      pygame.image.load("juego_parcial\enemigos/boss/boss_3.png"),
      pygame.image.load("juego_parcial\enemigos/boss/boss_4.png"),
      pygame.image.load("juego_parcial\enemigos/boss/boss_5.png"),
      pygame.image.load("juego_parcial\enemigos/boss/boss_daño.png")]


araña = [pygame.image.load("juego_parcial\enemigos/araña/7.png"),
         pygame.image.load("juego_parcial\enemigos/araña/8.png"),
         pygame.image.load("juego_parcial\enemigos/araña/9.png"),
         pygame.image.load("juego_parcial\enemigos/araña/10.png"),
         pygame.image.load("juego_parcial\enemigos/araña/12.png"),
         ]