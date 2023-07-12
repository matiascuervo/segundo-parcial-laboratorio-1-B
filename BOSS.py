import pygame
from animacion_enemigo import *
from proyectiles import*
from personaje import Personaje
from enemigo import Enemigo
from proyectil_enemigo import *
from proyectil_jefe import* 
import math

class Boss(Enemigo):
    def __init__(self, x_inicial, y_inicial, posicion_inicial, rango_movimiento, velocidad, lista_animaciones, width, height, cantidad_daño_personaje, cantidad_daño_proyectil, velocidad_animacion):
        super().__init__(x_inicial, y_inicial, posicion_inicial, velocidad, lista_animaciones, rango_movimiento, width, height, cantidad_daño_personaje, cantidad_daño_proyectil)
        self.x_inicial = x_inicial 
        self.y_inicial = y_inicial
        self.cooldown_disparo = 5000  # Tiempo de espera entre disparos (en milisegundos)
        self.tiempo_ultimo_disparo = pygame.time.get_ticks()
        self.lista_proyectiles_enemigo = pygame.sprite.Group()
        self.lista_animaciones = lista_animaciones
        self.rescalar_imagenes(width, height)
        self.rectangulo_personaje.width = width
        self.rectangulo_personaje.height = height
        self.cantidad_daño_personaje = cantidad_daño_personaje
        self.cantidad_daño_proyectil = cantidad_daño_proyectil
        self.indice_animacion = 0
        self.vida = 3000  # Vida inicial del enemigo
        self.cantidad_daño_personaje = cantidad_daño_personaje
        self.cantidad_daño_proyectil = cantidad_daño_proyectil
        self.vivo = True
        self.indice_animacion = 0
        self.velocidad_animacion = velocidad_animacion
        self.tiempo_ultima_animacion = pygame.time.get_ticks()  
    

    

    def update_animacion(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultima_animacion > self.velocidad_animacion:
            self.tiempo_ultima_animacion = tiempo_actual
            self.indice_animacion = (self.indice_animacion + 1) % len(self.lista_animaciones)
            self.image = self.lista_animaciones[self.indice_animacion]



    def update(self, PANTALLA):
        
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_disparo > self.cooldown_disparo:
            self.tiempo_ultimo_disparo = tiempo_actual
            self.disparar_proyectil(PANTALLA)
        
        self.update_animacion()



    def morir(self, pantalla, personaje):
        super().morir(pantalla, personaje)  # Llamar al método morir de la clase padre (Enemigo)
        personaje.puntos += 1000   
        



    def actualizar(self, personaje, lista_proyectiles, PANTALLA):
        if self.rango_movimiento is not None and isinstance(self.rango_movimiento, tuple):
            if self.rectangulo_enemigo.y >= int(self.rango_movimiento[1]):
                self.velocidad *= -1
            elif self.rectangulo_enemigo.y <= int(self.rango_movimiento[0]):
                self.velocidad *= -1

            self.rectangulo_enemigo.y += self.velocidad

        
            if personaje.rectangulo_personaje.colliderect(self.rectangulo_enemigo):
                self.recibir_daño(self.cantidad_daño_personaje,PANTALLA,personaje)
                

            for proyectil in lista_proyectiles:
                if proyectil.rect.colliderect(self.rectangulo_personaje):
                    print(self.vida)
                    self.recibir_daño(self.cantidad_daño_proyectil,PANTALLA,personaje) 
                    lista_proyectiles.remove(proyectil)

        
    def disparar_proyectil(self, PANTALLA):
       if self.vivo:
        proyectil_1 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, -5,-7)
        proyectil_3 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, -5,-5)
        proyectil_2 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, -5,-4)
        proyectil_4 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, -5,-3)
        proyectil_5 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, -5,0)
        proyectil_6 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, 5, 7)
        proyectil_7 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, 5, 6)
        proyectil_8 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, 5, 5)
        proyectil_9 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, 5, 3)
        proyectil_10 = Proyectil_enemigo_jefe(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, 5,2)   
        self.lista_proyectiles_enemigo.add(proyectil_1, proyectil_2, proyectil_3, proyectil_4,proyectil_5,proyectil_6,proyectil_7,proyectil_8,proyectil_9,proyectil_10)
        #self.lista_proyectiles_enemigo.add(proyectil_2)
        #PANTALLA.blit(proyectil.image, proyectil.rect)      