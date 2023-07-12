import pygame
import pygame.sprite
from personaje import Personaje
from animacion_enemigo import *
from animaciones import*
from proyectiles import*
import pygame.mixer

pygame.mixer.init()

class Enemigo(Personaje):
    def __init__(self, x_inicial, y_inicial, posicion_inicial, velocidad, lista_animaciones, rango_movimiento,width,height,cantidad_daño_personaje,cantidad_daño_proyectil):
        super().__init__(x_inicial, y_inicial, posicion_inicial, velocidad, lista_animaciones,cantidad_daño_personaje,cantidad_daño_proyectil)
        self.rango_movimiento = rango_movimiento
        self.direccion = 1
        self.lista_proyectiles_enemigo = []
        self.lista_animaciones_derecha = lista_animaciones[0]
        self.lista_animaciones_izquierda = lista_animaciones[1]
 
        self.rescalar_imagenes(width, height)
        self.rectangulo_enemigo = self.rectangulo_personaje
        # Ajustar el rectángulo del enemigo al tamaño del sprite
        self.rectangulo_enemigo.width = width
        self.rectangulo_enemigo.height = height
        self.vida = 20  # Vida inicial del enemigo
        self.cantidad_daño_personaje = cantidad_daño_personaje
        self.cantidad_daño_proyectil = cantidad_daño_proyectil
        self.vivo = True
        

    def actualizar(self, personaje, lista_proyectiles,PANTALLA):
        if self.rango_movimiento is not None:
            if isinstance(self.rango_movimiento, tuple):
                if self.rectangulo_enemigo.x >= int(self.rango_movimiento[1]):
                    self.direccion = -1  # Cambiar la dirección si llega al límite derecho
                    self.lista_animaciones = self.lista_animaciones_izquierda
                elif self.rectangulo_enemigo.x <= int(self.rango_movimiento[0]):
                    self.direccion = 1  # Cambiar la dirección si llega al límite izquierdo
                    self.lista_animaciones = self.lista_animaciones_derecha

                self.rectangulo_enemigo.x += self.velocidad * self.direccion
                self.rectangulo_enemigo.y = self.y_inicial  # Mantener la posición vertical constante

                if personaje.rectangulo_personaje.colliderect(self.rectangulo_enemigo):
                    self.recibir_daño(self.cantidad_daño_personaje,PANTALLA,personaje)  
                
    # Verificar colisión entre proyectiles y enemigo
            for proyectil in lista_proyectiles:
                if proyectil.rect.colliderect(self.rectangulo_enemigo):
                    self.recibir_daño(self.cantidad_daño_proyectil,PANTALLA,personaje)
                    lista_proyectiles.remove(proyectil)  


    def renderizar(self, pantalla):
        if self.vivo:
            if self.direccion == 1:
                self.animar_personaje(self.lista_animaciones_derecha, pantalla)
            else:
                self.animar_personaje(self.lista_animaciones_izquierda, pantalla)
        

    def recibir_daño(self, cantidad,PANTALLA,personaje):
        self.vida -= cantidad  
        if self.vida <= 0:
            self.morir(PANTALLA,personaje)  # Lógica para el enemigo al morir
   
    def morir(self, pantalla,personaje):
    # Lógica para el enemigo al morir
        self.velocidad = 10  # Velocidad de caída del enemigo
        self.direccion = 1  # Dirección de caída (hacia abajo)
        self.vivo = False
        personaje.puntos +=10
        
            


        sonido_muerte = pygame.mixer.Sound('./daño_enemigos.mp3')
      
        while self.rectangulo_enemigo.y < pantalla.get_height():
            self.rectangulo_enemigo.y += self.velocidad

            # Renderizar el enemigo en la nueva posición
            self.renderizar(pantalla)
            sonido_muerte.play()
            
        # Eliminar el enemigo de la lista de sprites
        self.rectangulo_enemigo.y = pantalla.get_height() + self.rectangulo_enemigo.height

      
        
           
