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

class Nivel():
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo,lista_enemigos,lista_proyectiles,lista_estrellas,lista_corazones,W,que_nivel):
        self.pantalla = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = pygame.image.load(imagen_fondo)
        self.lista_enemigos = lista_enemigos
        self.lista_proyectiles= lista_proyectiles
        self.que_hace = "quieto"
        self.lista_estrellas=lista_estrellas
        self.lista_corazones=lista_corazones
        self.contador_estrellas = 0
        self.width = W
        self.piso = self.crear_piso(0,0, W)
        self.proyectiles = pygame.sprite.Group()
        self.que_nivel = que_nivel 
        self.sonido_ataque = pygame.mixer.Sound("Arrow_Hit_DamageAdd_WeakHit.wav")
    def update(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()  
        
    def crear_piso(self, x_piso, y_piso, W):
        piso = pygame.Rect(x_piso, y_piso, W, 20)
        offset = 20  # Cantidad de desplazamiento hacia arriba
        piso.y = self.pantalla.get_height() - piso.height - offset  # Posición y ligeramente por encima de la parte inferior de la pantalla
        return piso

        
    def generarNivel(self,ruta_fondo):
        self.img_fondo = pygame.image.load(ruta_fondo)
        self.img_fondo = pygame.transform.scale(self.img_fondo,(1000,700))
        self.actualizar_pantalla(self.pantalla, self.que_hace, 0, self.piso, self.width)
    
    
    
        
    def leer_input(self,keys,PANTALLA,W):
        
        if keys[pygame.K_RIGHT]:
            self.que_hace = "derecha"
        elif keys[pygame.K_LEFT]:
            self.que_hace = "izquierda"
        elif keys[pygame.K_UP]:
           self.que_hace ="saltar"
        elif  keys[pygame.K_x]:
            self.que_hace ="ataque"
            self.sonido_ataque.play()
            nuevo_proyectil = Proyectil(self.jugador.rectangulo_personaje.centerx, self.jugador.rectangulo_personaje.centery, 10)
            if self.jugador.mirando_izquierda:
                nuevo_proyectil.velocidad *= -1
                nuevo_proyectil.imagenes = girar_imagenes(nuevo_proyectil.imagenes, True, False)
            self.lista_proyectiles.append(nuevo_proyectil)         
        else:
            self.que_hace = "quieto"

        #self.jugador.aplicar_gravedad(PANTALLA, personaje_salta if not self.jugador.mirando_izquierda else personaje_salta_izquierda, self.jugador.rectangulo_personaje, self.plataformas, self.piso)
       
        
        self.actualizar_pantalla(self.pantalla, self.que_hace, 0, self.piso, self.width) 
        self.verificar_enemigos_vivos(PANTALLA)
        self.renderizar_proyectiles_enemigos(PANTALLA)
        self.mostrar_proyectiles(PANTALLA,W)
        self.renderizar_estrellas(PANTALLA)
        self.renderizar_corazones(PANTALLA)
        self.verificar_vida(PANTALLA)
        self.jugador.recibir_daño_heroe(50, self.lista_enemigos)

        
        


    def dibujar_rectangulos(self):
        if get_mode() == True:
            pygame.draw.rect(self._slave,"BLUE", self.jugador.rectangulo_personaje,2)


        for proyectil in self.lista_proyectiles:
             pygame.draw.rect(self._slave, (255, 0, 0), proyectil.rect, 2)


    def actualizar_pantalla(self,PANTALLA,que_hace,velocidad,piso,W):
        PANTALLA.blit(self.img_fondo, (0,0))
        #PANTALLA.blit(plataforma,(lista_plataformas[0].x,lista_plataformas[0].y))
        for plataforma in self.plataformas:
            PANTALLA.blit(plataforma.sprites_plataforma[self.que_nivel],(plataforma.x_inicial, plataforma.y_inicial))
            
        
        fondo_puntos = pygame.image.load("./plataformas/5.png")
        PANTALLA.blit(fondo_puntos,(10,10))
        fuente_Georgia = pygame.font.SysFont("Georgia", 24)
        texto_puntos = fuente_Georgia.render("Puntos: " + str(self.jugador.puntos), True, (255, 255, 255))
        PANTALLA.blit(texto_puntos, (15, 10))
        
        
        fuente_arialblack = pygame.font.SysFont("arialblack", 24)
        texto_estrellas = fuente_arialblack.render("Estrellas: " + str(self.contador_estrellas), True, (255, 255, 0))
        PANTALLA.blit(texto_estrellas, (20, 89))

        
        match que_hace:
            case "derecha":
                    if not self.jugador.esta_saltando:
                        self.jugador.animar_personaje(personaje_camina,PANTALLA)
                        self.jugador.mirando_izquierda = False 
                    self.jugador.mover_personaje(self.jugador.velocidad,W)
            case "quieto":
                if not self.jugador.esta_saltando:
                    if self.jugador.mirando_izquierda ==True:
                        self.jugador.animar_personaje(personaje_quieto_izquierda, PANTALLA)
                    else:    
                        self.jugador.animar_personaje(personaje_quieto,PANTALLA)
            case "izquierda":
                    if not self.jugador.esta_saltando:
                        self.jugador.animar_personaje(personaje_camina_izquierda,PANTALLA)
                        self.jugador.mirando_izquierda = True
                    self.jugador.mover_personaje(self.jugador.velocidad*-1,W)
            case "saltar":
                if not self.jugador.esta_saltando:
                    self.jugador.esta_saltando = True
                    self.jugador.desplazamiento_y = self.jugador.potencia_salto
                if self.jugador.mirando_izquierda:
                    self.jugador.animar_personaje(personaje_salta_izquierda, PANTALLA)
                else:
                    self.jugador.animar_personaje(personaje_salta, PANTALLA)  
            case "ataque":
                    if not self.jugador.esta_saltando:        
                        if self.jugador.mirando_izquierda:
                            self.jugador.animar_personaje(personaje_ataque_izquierda,PANTALLA)
                        else: self.jugador.animar_personaje(personaje_ataque,PANTALLA)                      
                        
                    
        self.jugador.aplicar_gravedad(PANTALLA, personaje_salta if not self.jugador.mirando_izquierda else personaje_salta_izquierda, self.jugador.rectangulo_personaje, self.plataformas, self.piso)



    def verificar_vida(self,PANTALLA,):
        self.jugador.vida_personaje(PANTALLA,self.jugador.imagen_corazon)
        


    def renderizar_proyectiles_enemigos(self, PANTALLA):
        for enemigo in self.lista_enemigos:
            if isinstance(enemigo, PlantaEnemigo):
                enemigo.update(PANTALLA)
                for proyectil in enemigo.lista_proyectiles_enemigo:
                    proyectil.update()
                    PANTALLA.blit(proyectil.image, proyectil.rect)
            
    def mostrar_proyectiles(self, PANTALLA,W):
        for proyectil in self.lista_proyectiles:
            PANTALLA.blit(proyectil.image, proyectil.rect)
            proyectil.update()

        for proyectil in self.lista_proyectiles.copy():
            if proyectil.rect.x > W:
                self.lista_proyectiles.remove(proyectil)
            

    def renderizar_proyectiles_heroe(self, PANTALLA, W):
        for proyectil in self.lista_proyectiles:
            proyectil.update()
            PANTALLA.blit(proyectil.image, proyectil.rect)

        for proyectil in self.lista_proyectiles.copy():
            if proyectil.rect.x > W:
                self.lista_proyectiles.remove(proyectil)

    def renderizar_estrellas(self,PANTALLA):
        for estrella in self.lista_estrellas:
            estrella.update()
            estrella.renderizar_item(PANTALLA)
            if self.jugador.rectangulo_personaje.colliderect(estrella.rectangulo_item):
                estrella.colision_personaje_items(self.jugador.rectangulo_personaje,self.jugador.vida_heroe)
                self.contador_estrellas+=1
                self.lista_estrellas.remove(estrella)
        
    
    def renderizar_corazones(self,PANTALLA):
        for corazon in self.lista_corazones:
            corazon.update()
            corazon.renderizar_item(PANTALLA)
            if self.jugador.rectangulo_personaje.colliderect(corazon.rectangulo_item):
                nueva_vida_heroe = corazon.colision_personaje_items(self.jugador.rectangulo_personaje, self.jugador.vida_heroe)
                self.jugador.vida_heroe = nueva_vida_heroe    
                self.lista_corazones.remove(corazon)

    
    
        

    def verificar_enemigos_vivos(self,PANTALLA):
        for enemigo in self.lista_enemigos:
            if enemigo.vivo:
                enemigo.actualizar(self.jugador, self.lista_proyectiles, PANTALLA)
                enemigo.renderizar(PANTALLA)
                planta_tru = isinstance(enemigo,PlantaEnemigo) 
                if planta_tru == True:
                    enemigo.daño_planta(PANTALLA,self.jugador,self.lista_proyectiles)
                        