import pygame
from animaciones import*
import time
import sys

#sonido_muerte_planta = pygame.mixer.Sound('juego_parcial\SE_KeeseSwarm_Attack.wav')

class Personaje():
    def __init__(self,x_inicial,y_inicial,posicion_inicial,velocidad,lista_animaciones,cantidad_daño_personaje,cantidad_daño_proyectil):

        self.contador_pasos = 0
        self.x_inicial =x_inicial
        self.y_inicial = y_inicial
        self.posicion_inicial_X = posicion_inicial
        self.velocidad = velocidad
        self.lista_animaciones= lista_animaciones
        self.rescalar_imagenes(75, 85)
        self.rectangulo_personaje = personaje_salta[0].get_rect()
        self.rectangulo_personaje.x = x_inicial
        self.rectangulo_personaje.y = y_inicial
        self.puntos = 0
        self.vida_heroe = 300
        self.vidas = 3
        self.heroe_vivo = True
        self.imagen_corazon = pygame.image.load("./vida_estrellas/0.png")
        self.cantidad_daño_personaje = cantidad_daño_personaje
        self.cantidad_daño_proyectil = cantidad_daño_proyectil
        self.personaje_muerte = personaje_muerte
        self.sprites_corazones = []  # Lista para almacenar las imágenes de los corazones
        self.cargar_sprites_corazones()  
        self.tiempo_animacion_daño = 0
        self.parpadeando = False
        self.animacion_muerte_reproducida = False
        self.gravedad = 1
        self.potencia_salto = -20
        self.limite_velocidad_caida = 10
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.mirando_izquierda = False
        

    def cargar_sprites_corazones(self):
        self.sprites_corazones = []  # Reiniciar la lista de sprites de corazones
        imagen_corazon = pygame.image.load("./vida_estrellas/0.png")

        for _ in range(self.vidas):
            self.sprites_corazones.append(imagen_corazon.copy())

        return imagen_corazon    

                     
 # Eliminar el último sprite de corazón de la lista



    def rescalar_imagenes(self, width, height):
        for animacion in self.lista_animaciones:
            for i in range(len(animacion)):
                animacion[i] = pygame.transform.scale(animacion[i], (width, height))

    def mover_personaje(self,velocidad,W):
        self.rectangulo_personaje.x +=velocidad
        if self.rectangulo_personaje.left < 0:
            self.rectangulo_personaje.left = 0
        elif self.rectangulo_personaje.right > W:
            self.rectangulo_personaje.right = W

        #if self.rectangulo_personaje.top < 0:
        #    self.rectangulo_personaje.top = 0
        #elif self.rectangulo_personaje.bottom > H:
        #    self.rectangulo_personaje.bottom = H


    def animar_personaje(self, accion_personaje, PANTALLA):
        if self.parpadeando:
            tiempo_actual = pygame.time.get_ticks()
            duracion_parpadeo = 1000  # Duración en milisegundos del parpadeo

            if tiempo_actual - self.tiempo_animacion_daño >= duracion_parpadeo:
                self.parpadeando = False
            elif (tiempo_actual - self.tiempo_animacion_daño) % 200 < 100:
                # Muestra el sprite del personaje solo durante 100 milisegundos cada 200 milisegundos
                if self.contador_pasos < len(accion_personaje):
                    PANTALLA.blit(accion_personaje[self.contador_pasos], self.rectangulo_personaje)
                    self.contador_pasos += 1
        else:
            if self.contador_pasos < len(accion_personaje):
                PANTALLA.blit(accion_personaje[self.contador_pasos], self.rectangulo_personaje)
                self.contador_pasos += 1

        if self.contador_pasos >= len(accion_personaje):
            self.contador_pasos = 0


        
              
    def obtener_rectangulos(self):
        diccionario = {}

        diccionario["main"] = self.rectangulo_personaje
        diccionario["bottom"] = pygame.Rect(self.rectangulo_personaje.left, self.rectangulo_personaje.bottom - 6, self.rectangulo_personaje.width, 6)
        diccionario["right"] = pygame.Rect(self.rectangulo_personaje.right + 2, self.rectangulo_personaje.top, 2, self.rectangulo_personaje.height)
        diccionario["left"] = pygame.Rect(self.rectangulo_personaje.left, self.rectangulo_personaje.top, 2, self.rectangulo_personaje.height)
        diccionario["top"] = pygame.Rect(self.rectangulo_personaje.left, self.rectangulo_personaje.top, self.rectangulo_personaje.width, 6)
        
        return diccionario
            
        
    def recibir_daño_heroe(self, cantidad, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.rectangulo_personaje.colliderect(enemigo.rectangulo_enemigo):
                self.vida_heroe -= cantidad
                self.parpadeando = True
                self.tiempo_animacion_daño = pygame.time.get_ticks()
                # Resto de la lógica cuando el personaje recibe daño de un enemigo
                return True
            if enemigo.lista_proyectiles_enemigo:
                for proyectil in enemigo.lista_proyectiles_enemigo:
                    if self.rectangulo_personaje.colliderect(proyectil.rect):
                        self.vida_heroe -= cantidad
                        enemigo.lista_proyectiles_enemigo.remove(proyectil)
                        self.parpadeando = True
                        self.tiempo_animacion_daño = pygame.time.get_ticks()
                        return True
        return False 

    def morir_heroe(self, pantalla):
    # Lógica para el enemigo al morir
        if self.heroe_vivo == False:
            self.lista_animaciones= self.personaje_muerte
            imagen_game = pygame.image.load("./formularios\cosas_formularios/11.png")
            imagen_over = pygame.image.load("./formularios\cosas_formularios/12.png")
            pantalla.blit(imagen_game, (350,350))  # Especifica las coordenadas x e y de la imagen "game"
            pantalla.blit(imagen_over, (450,350))  # Especifica las coordenadas x e y de la imagen "over"
            #pygame.display.flip()  # Actualiza la pantalla
            #pygame.time.wait(3000)
            

        


    def vida_personaje(self, pantalla,imagen_corazon):
        x = 20  # Posición x inicial para los corazones
        y = 61  # Posición y para los corazones

        for sprite_corazon in self.sprites_corazones:
            pantalla.blit(sprite_corazon, (x, y))
            x += sprite_corazon.get_width() + 5

        if self.vida_heroe < self.vidas * 100:
            self.vidas -= 1
            if self.vidas < len(self.sprites_corazones):
                if self.sprites_corazones:
                    self.sprites_corazones.pop()
        if self.vida_heroe > self.vidas * 100:
            while self.vidas < self.vida_heroe // 100:
                self.sprites_corazones.append(imagen_corazon)
                self.vidas += 1 
        if self.vidas == 0:
            self.heroe_vivo = False
            self.morir_heroe(pantalla)  



    def aumentar_vida(self, cantidad):
        self.vida_heroe += cantidad



    def derecha(self, PANTALLA, velocidad, W):
        if not self.esta_saltando:
            self.animar_personaje(personaje_camina, PANTALLA)
            self.mirando_izquierda = False 
        self.mover_personaje(velocidad, W)

    def izquierda(self, PANTALLA, velocidad, W):
        if not self.esta_saltando:
            self.animar_personaje(personaje_camina_izquierda, PANTALLA)
            self.mirando_izquierda = True
        self.mover_personaje(velocidad * -1, W)

    def quieto(self, PANTALLA):
        if not self.esta_saltando:
            if self.mirando_izquierda:
                self.animar_personaje(personaje_quieto_izquierda, PANTALLA)
            else:
                self.animar_personaje(personaje_quieto, PANTALLA)

    def saltar(self, PANTALLA):
        if not self.esta_saltando:
            self.esta_saltando = True
            self.desplazamiento_y = self.potencia_salto
        if self.mirando_izquierda:
            self.animar_personaje(personaje_salta_izquierda, PANTALLA)
        else:
            self.animar_personaje(personaje_salta, PANTALLA)

    def ataque(self, PANTALLA):
        if not self.esta_saltando:
            if self.mirando_izquierda:
                self.animar_personaje(personaje_ataque_izquierda, PANTALLA)
            else:
                self.animar_personaje(personaje_ataque, PANTALLA)

    
   

      # Variable para verificar si hay colisión con alguna plataforma

    def aplicar_gravedad(self, pantalla, personaje_accion, rectangulo_personaje, plataformas, piso):
        colisionando = False  # Variable para verificar si hay colisión con alguna plataforma

        if self.esta_saltando:
            self.animar_personaje(personaje_accion, pantalla)
            rectangulo_personaje.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        # Verificar colisión con las plataformas
        for plataforma in plataformas:
            if rectangulo_personaje.colliderect(plataforma.rectangulo_plataforma):
                colisionando = True  # Hay colisión con una plataforma
                if self.desplazamiento_y > 0:
                    # Colisión con el borde inferior de la plataforma
                    # No permitir que el personaje pase a través de la plataforma
                    rectangulo_personaje.bottom = plataforma.rectangulo_plataforma.top
                    self.esta_saltando = False
                    self.desplazamiento_y = 0
                elif self.desplazamiento_y < 0:
                    # Colisión con el borde superior de la plataforma
                    # Permitir que el personaje se quede sobre la plataforma
                    rectangulo_personaje.top = plataforma.rectangulo_plataforma.bottom
                    self.desplazamiento_y = 0
                else:
                    # Colisión con los lados de la plataforma
                    if rectangulo_personaje.right > plataforma.rectangulo_plataforma.left and rectangulo_personaje.left < plataforma.rectangulo_plataforma.right:
                        if self.desplazamiento_y == 0 and rectangulo_personaje.centery == plataforma.rectangulo_plataforma.centery:
                            # Ajustar la posición vertical solo si el personaje está en el mismo nivel vertical que la plataforma
                            if rectangulo_personaje.right < plataforma.rectangulo_plataforma.centerx:
                                # Colisión con el borde izquierdo de la plataforma
                                rectangulo_personaje.right = plataforma.rectangulo_plataforma.left
                            else:
                                # Colisión con el borde derecho de la plataforma
                                rectangulo_personaje.left = plataforma.rectangulo_plataforma.right

                if rectangulo_personaje.bottom == plataforma.rectangulo_plataforma.top:
                    self.esta_saltando = False
                    self.desplazamiento_y = 0

        # Verificar colisión con el piso
        if rectangulo_personaje.colliderect(piso):
            colisionando = True  # Hay colisión con el piso
            rectangulo_personaje.bottom = piso.top
            self.esta_saltando = False
            self.desplazamiento_y = 0

        # Si no hay colisión con ninguna plataforma ni con el piso, aplicar la gravedad
        if not colisionando and not self.esta_saltando:
            rectangulo_personaje.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        colisionando = False

        

