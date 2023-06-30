import pygame
from enemigo import Enemigo
from proyectil_enemigo import *
import random


class PlantaEnemigo(Enemigo):
    def __init__(self, piso, posicion_inicial, rango_movimiento, velocidad, lista_animaciones, lista_proyectiles, width, height, cantidad_daño_personaje, cantidad_daño_proyectil,velocidad_animacion):
        x_inicial = random.randint(piso.left, piso.right - width)
        y_inicial = piso.top - height
        super().__init__(x_inicial, y_inicial, posicion_inicial, velocidad, lista_animaciones, rango_movimiento, width, height, cantidad_daño_personaje, cantidad_daño_proyectil)
        self.cooldown_disparo = 2000  # Tiempo de espera entre disparos (en milisegundos)
        self.tiempo_ultimo_disparo = pygame.time.get_ticks()
        self.lista_proyectiles_enemigo = pygame.sprite.Group()
        self.lista_animaciones= lista_animaciones
        self.rescalar_imagenes(width,height)
        self.rectangulo_personaje.width = width
        self.rectangulo_personaje.height = height
        self.cantidad_daño_personaje = cantidad_daño_personaje
        self.cantidad_daño_proyectil = cantidad_daño_proyectil
        self.velocidad_animacion = velocidad_animacion
        self.tiempo_ultima_animacion = pygame.time.get_ticks()
        self.indice_animacion = 0
        
    
        
    def update(self):
        # Actualizar animación y posición del enemigo

        # Verificar si es el momento de disparar un proyectil
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_disparo > self.cooldown_disparo:
            self.tiempo_ultimo_disparo = tiempo_actual
            self.disparar_proyectil()

        self.update_animacion()

    def update_animacion(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultima_animacion > self.velocidad_animacion:
            self.tiempo_ultima_animacion = tiempo_actual
            self.indice_animacion = (self.indice_animacion + 1) % len(self.lista_animaciones)
            self.image = self.lista_animaciones[self.indice_animacion]
            

    def disparar_proyectil(self):
        proyectil = Proyectil_enemigo(self.rectangulo_personaje.centerx, self.rectangulo_personaje.centery, velocidad=-5)
        self.lista_proyectiles_enemigo.add(proyectil)


    def daño_planta(self,PANTALLA,personaje,lista_proyectiles):
        if personaje.rectangulo_personaje.colliderect(self.rectangulo_personaje):
                self.recibir_daño(self.cantidad_daño_personaje,PANTALLA,personaje)  

    # Verificar colisión entre proyectiles y enemigo
        for proyectil in lista_proyectiles:
            if proyectil.rect.colliderect(self.rectangulo_personaje):
                self.recibir_daño(self.cantidad_daño_proyectil,PANTALLA,personaje)  