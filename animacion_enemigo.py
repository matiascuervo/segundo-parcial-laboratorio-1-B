import pygame
from animaciones import*

gusano = [
    pygame.image.load("./enemigos\gusanito/0.png"),
    pygame.image.load("./enemigos\gusanito/1.png"),
    pygame.image.load("./enemigos\gusanito/2.png"),
    pygame.image.load("./enemigos\gusanito/3.png")
]

gusano_izquierda=[
    pygame.image.load("./enemigos\gusanito/4.png"),
    pygame.image.load("./enemigos\gusanito/5.png"),
    pygame.image.load("./enemigos\gusanito/6.png"),
    pygame.image.load("./enemigos\gusanito/7.png")]

gusano_muerto =girar_imagenes(gusano,False,True)

troll=[pygame.image.load("./enemigos/troll/22.png"),
       pygame.image.load("./enemigos/troll/23.png"),
       pygame.image.load("./enemigos/troll/24.png"),]

troll_derecha=girar_imagenes(troll,True,False)

planta=[pygame.image.load("./enemigos\planta/17.png"),
        pygame.image.load("./enemigos\planta/18.png"),
        pygame.image.load("./enemigos\planta/19.png"),
        pygame.image.load("./enemigos\planta/20.png")]
planta_izquierda =girar_imagenes(planta,True,False)
lista_animaciones_planta = [planta,planta_izquierda]
boss=[pygame.image.load("./enemigos/boss/boss_0.png"),
      pygame.image.load("./enemigos/boss/boss_1.png"),
      pygame.image.load("./enemigos/boss/boss_2.png"),
      pygame.image.load("./enemigos/boss/boss_3.png"),
      pygame.image.load("./enemigos/boss/boss_4.png"),
      pygame.image.load("./enemigos/boss/boss_5.png"),
      ]

boss_daño=[pygame.image.load("./enemigos/boss/boss_daño.png")]

araña = [pygame.image.load("./enemigos/araña/7.png"),
         pygame.image.load("./enemigos/araña/8.png"),
         pygame.image.load("./enemigos/araña/9.png"),
         pygame.image.load("./enemigos/araña/10.png"),
         pygame.image.load("./enemigos/araña/12.png"),
         ]