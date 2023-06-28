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
pygame.init()
#PANTALLA///////////////////////////////////////////
W,H = 1000,700
TAMAÑO_PANTALLA= (W,H)

FPS = 15

clock = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))

fondo_pantalla = pygame.image.load("juego_parcial/mapa/mapa_1.jpg")
fondo_escalado = pygame.transform.scale(fondo_pantalla, TAMAÑO_PANTALLA)

COLOR_NEGRO = (0, 0, 0)
COLOR_FONDO = COLOR_NEGRO
#PANTALLA///////////////////////////////////////////

mirando_izquierda = False
plataforma = Plataforma(100,300,0,(200,75),0)
plataforma_2 = Plataforma(800,300,0,(200,75),0)
plataforma_3 = Plataforma(500,120,0,(300,75),2)
plataformas=[plataforma,plataforma_2,plataforma_3]

def actualizar_pantalla(PANTALLA,que_hace,velocidad,piso):
    PANTALLA.blit(fondo_escalado, (0,0))
    #PANTALLA.blit(plataforma,(lista_plataformas[0].x,lista_plataformas[0].y))
    PANTALLA.blit(plataforma.sprites_plataforma[0],(plataforma.x_inicial,plataforma.y_inicial))
    PANTALLA.blit(plataforma_2.sprites_plataforma[0],(plataforma_2.x_inicial,plataforma_2.y_inicial))
    PANTALLA.blit(plataforma_3.sprites_plataforma[0],(plataforma_3.x_inicial,plataforma_3.y_inicial))
    #PANTALLA.blit()

    fondo_puntos = pygame.image.load("juego_parcial\plataformas/5.png")
    PANTALLA.blit(fondo_puntos,(10,10))
    fuente_Georgia = pygame.font.SysFont("Georgia", 24)
    texto_puntos = fuente_Georgia.render("Puntos: " + str(personaje.puntos), True, (255, 255, 255))
    PANTALLA.blit(texto_puntos, (15, 10))

    global esta_saltando 
    global desplazamiento_y
    global mirando_izquierda 
    match que_hace:
         case "derecha":
                if not esta_saltando:
                    personaje.animar_personaje(personaje_camina,PANTALLA)
                    mirando_izquierda = False 
                personaje.mover_personaje(velocidad,W)
         case "quieto":
             if not esta_saltando:
                if mirando_izquierda ==True:
                    personaje.animar_personaje(personaje_quieto_izquierda, PANTALLA)
                else:    
                    personaje.animar_personaje(personaje_quieto,PANTALLA)
         case "izquierda":
                if not esta_saltando:
                    personaje.animar_personaje(personaje_camina_izquierda,PANTALLA)
                    mirando_izquierda = True
                personaje.mover_personaje(velocidad*-1,W)
         case "saltar":
             if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
             if mirando_izquierda:
                personaje.animar_personaje(personaje_salta_izquierda, PANTALLA)
             else:
                personaje.animar_personaje(personaje_salta, PANTALLA)  
         case "ataque":
                if not esta_saltando:        
                    if mirando_izquierda:
                        personaje.animar_personaje(personaje_ataque_izquierda,PANTALLA)
                    else: personaje.animar_personaje(personaje_ataque,PANTALLA)   
    aplicar_gravedad(PANTALLA, personaje_salta if not mirando_izquierda else personaje_salta_izquierda, personaje.rectangulo_personaje, plataformas, piso)



gravedad = 1
potencia_salto = -20
limite_velociad_caida = 15
esta_saltando = False
desplazamiento_y = 0

def aplicar_gravedad(PANTALLA, personaje_accion, rectangulo_personaje, plataformas, piso):
    global desplazamiento_y, esta_saltando

    colisionando = False  # Variable para verificar si hay colisión con alguna plataforma

    if esta_saltando:
        personaje.animar_personaje(personaje_accion, PANTALLA)
        rectangulo_personaje.y += desplazamiento_y
        if desplazamiento_y + gravedad < limite_velociad_caida:
            desplazamiento_y += gravedad

    # Verificar colisión con las plataformas
    for plataforma in plataformas:
        if rectangulo_personaje.colliderect(plataforma.rectangulo_plataforma):
            colisionando = True  # Hay colisión con una plataforma
            if desplazamiento_y > 0:
                # Colisión con el borde inferior de la plataforma
                # No permitir que el personaje pase a través de la plataforma
                rectangulo_personaje.bottom = plataforma.rectangulo_plataforma.top 
                esta_saltando = False
                desplazamiento_y = 0
            elif desplazamiento_y < 0:
                # Colisión con el borde superior de la plataforma
                # Permitir que el personaje se quede sobre la plataforma
                rectangulo_personaje.top = plataforma.rectangulo_plataforma.bottom
                desplazamiento_y = 0
            else:
                # Colisión con los lados de la plataforma
                # Colisión con los lados de la plataforma
                if rectangulo_personaje.right > plataforma.rectangulo_plataforma.left and rectangulo_personaje.left < plataforma.rectangulo_plataforma.right:
                    if desplazamiento_y == 0 and rectangulo_personaje.centery == plataforma.rectangulo_plataforma.centery:
                        # Ajustar la posición vertical solo si el personaje está en el mismo nivel vertical que la plataforma
                        if rectangulo_personaje.right < plataforma.rectangulo_plataforma.centerx:
                            # Colisión con el borde izquierdo de la plataforma
                            rectangulo_personaje.right = plataforma.rectangulo_plataforma.left
                        else:
                            # Colisión con el borde derecho de la plataforma
                            rectangulo_personaje.left = plataforma.rectangulo_plataforma.right



            if rectangulo_personaje.bottom == plataforma.rectangulo_plataforma.top:
                esta_saltando = False
                desplazamiento_y = 0

    # Verificar colisión con el piso
    if rectangulo_personaje.colliderect(piso):
        colisionando = True  # Hay colisión con el piso
        rectangulo_personaje.bottom = piso.top
        esta_saltando = False
        desplazamiento_y = 0

    # Si no hay colisión con ninguna plataforma, aplicar la gravedad
    if not colisionando and not esta_saltando:
        rectangulo_personaje.y += desplazamiento_y
        if desplazamiento_y + gravedad < limite_velociad_caida:
            desplazamiento_y += gravedad

    colisionando = False  # Reiniciar la variable a False para el siguiente ciclo



# Colisión del personaje con las plataformas
    
#PERSONAJE//////////////////////////////////////
personaje = Personaje(H/2 - 300, 450, 0, 10,[personaje_camina,
                   personaje_quieto,
                   personaje_salta,
                   personaje_cae_salto,
                   personaje_ataque,
                   personaje_daño,
                   personaje_camina_izquierda,
                   personaje_quieto_izquierda,
                   personaje_salta_izquierda,
                   personaje_ataque_izquierda])



#gusano = Enemigo(189, 275, 0, 10, [gusano, gusano_izquierda])
gusano_enemigo_3 = Enemigo(889,270, 0, 5, [gusano, gusano_izquierda], (805, 950), 30, 35, 10, 5)
gusano_enemigo_2 = Enemigo(581, 90, 0, 5, [gusano, gusano_izquierda], (502, 789), 30, 35, 10, 5)
gusano_enemigo = Enemigo(189, 275, 0, 5, [gusano, gusano_izquierda], (102, 296), 30, 35, 10, 5)
gusano_enemigo.cantidad_daño_personaje = 10  # Cantidad de daño que recibe el enemigo cuando es golpeado por el personaje
gusano_enemigo.cantidad_daño_proyectil = 5  # Cantidad de daño que recibe el enemigo cuando es golpeado por un proyectil

gusano_enemigo_2.cantidad_daño_personaje = 10
gusano_enemigo_2.cantidad_daño_proyectil = 5

gusano_enemigo_3.cantidad_daño_personaje = 10
gusano_enemigo_3.cantidad_daño_proyectil = 5


#rescalar_imagenes(lista_animaciones,75,85)


que_hace = "quieto"
pygame.mixer.music.load("juego_parcial\Arrow_Hit_DamageAdd_WeakHit.wav")
#PISO//////////////////
piso = pygame.Rect(0,0,W,20)
piso.top = personaje.rectangulo_personaje.bottom
lista_proyectiles = []
lista_proyectiles_enemigo=[]
x_piso = random.randint(piso.left, piso.right)
y_piso = piso.top - 75  # Ajusta la altura de la planta según tus necesidades

proyectiles = pygame.sprite.Group()
planta_enemigo = PlantaEnemigo(piso, x_piso, y_piso, 0, lista_animaciones_planta, proyectiles, 50, 50, 10, 5,200)
planta_enemigo_2 = PlantaEnemigo(piso, x_piso, y_piso, 0, lista_animaciones_planta, proyectiles, 50, 50, 10, 5,200)
#planta_proyectil = Proyectil_enemigo(planta_enemigo.rectangulo_personaje.centerx, personaje.rectangulo_personaje.centery, -10)
#planta_enemigo.lista_proyectiles_enemigo.add(planta_proyectil)
planta_enemigo.cantidad_daño_personaje = 10
planta_enemigo.cantidad_daño_proyectil = 5


while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        que_hace ="saltar"
    elif  keys[pygame.K_x]:
        que_hace ="ataque"
        pygame.mixer.music.play(1)
        nuevo_proyectil = Proyectil(personaje.rectangulo_personaje.centerx, personaje.rectangulo_personaje.centery, 10)
        if mirando_izquierda:
            nuevo_proyectil.velocidad *= -1
            nuevo_proyectil.imagenes = girar_imagenes(nuevo_proyectil.imagenes, True, False)
        lista_proyectiles.append(nuevo_proyectil)        
    else:
        que_hace = "quieto"
    
    
    actualizar_pantalla(PANTALLA, que_hace, personaje.velocidad,piso)
   
    #mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(f"Coordenadas del cursor del mouse: ({mouse_x}, {mouse_y})")
    if get_mode() == True:
        pygame.draw.rect(PANTALLA,"BLUE", personaje.rectangulo_personaje,2)
        pygame.draw.rect(PANTALLA,"RED", piso,2)
        pygame.draw.rect(PANTALLA,"RED",plataforma.rectangulo_plataforma,2)
        pygame.draw.rect(PANTALLA,"RED",plataforma_2.rectangulo_plataforma,2)
        pygame.draw.rect(PANTALLA,"RED",plataforma_3.rectangulo_plataforma,2)
        pygame.draw.rect(PANTALLA, (0, 0, 255), plataforma.obtener_rectangulos()["bottom"], 2)
        pygame.draw.rect(PANTALLA, (0, 0, 0), personaje.obtener_rectangulos()["left"], 2)
        pygame.draw.rect(PANTALLA,"RED",gusano_enemigo.rectangulo_personaje,2)
        if get_mode():
            for proyectil in lista_proyectiles:
             pygame.draw.rect(PANTALLA, (255, 0, 0), proyectil.rect, 2)

    

    
    if gusano_enemigo.vivo:
        gusano_enemigo.actualizar(personaje, lista_proyectiles, PANTALLA)
        gusano_enemigo.renderizar(PANTALLA)
    if gusano_enemigo_2.vivo:
        gusano_enemigo_2.actualizar(personaje, lista_proyectiles, PANTALLA)
        gusano_enemigo_2.renderizar(PANTALLA)
    if gusano_enemigo_3.vivo:
        gusano_enemigo_3.actualizar(personaje, lista_proyectiles, PANTALLA)
        gusano_enemigo_3.renderizar(PANTALLA)
    
    if planta_enemigo.vivo:
        
        planta_enemigo.renderizar(PANTALLA)
        planta_enemigo.update() 
        planta_enemigo.daño_planta(PANTALLA,personaje,lista_proyectiles)
    if planta_enemigo_2.vivo:
        planta_enemigo_2.renderizar(PANTALLA)
        planta_enemigo_2.update() 
        planta_enemigo_2.daño_planta(PANTALLA,personaje,lista_proyectiles)
        

        
    for proyectil in planta_enemigo.lista_proyectiles_enemigo:
        proyectil.update()
        PANTALLA.blit(proyectil.image, proyectil.rect)
    for proyectil in planta_enemigo_2.lista_proyectiles_enemigo:
        proyectil.update()
        PANTALLA.blit(proyectil.image, proyectil.rect)
    
        
    proyectiles.draw(PANTALLA)
    proyectiles.update()
    

    for proyectil in lista_proyectiles:
        proyectil.update()
        PANTALLA.blit(proyectil.image, proyectil.rect)
    for proyectil in lista_proyectiles.copy():
        if proyectil.rect.x > W:
            lista_proyectiles.remove(proyectil)    


    pygame.display.update()     
    #pygame.time.delay(50)
