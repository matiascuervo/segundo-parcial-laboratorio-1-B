import pygame
import pygame.sprite
from personaje import Personaje
from animacion_enemigo import *
from animaciones import*
from proyectiles import*
import pygame.mixer

pygame.mixer.init()
sonido_muerte = pygame.mixer.Sound('juego_parcial\Squirrel_Vo_Wait4.wav')
sonido_muerte_planta = pygame.mixer.Sound('juego_parcial\SE_KeeseSwarm_Attack.wav')
class Enemigo(Personaje):
    def __init__(self, x_inicial, y_inicial, posicion_inicial, velocidad, lista_animaciones, rango_movimiento,width,height,cantidad_daño_personaje,cantidad_daño_proyectil):
        super().__init__(x_inicial, y_inicial, posicion_inicial, velocidad, lista_animaciones)
        self.rango_movimiento = rango_movimiento
        self.direccion = 1
        self.lista_animaciones_derecha = lista_animaciones[0]
        self.lista_animaciones_izquierda = lista_animaciones[1]
        self.lista_animaciones_muerte = gusano_muerto
        self.rescalar_imagenes(width, height)

        # Ajustar el rectángulo del enemigo al tamaño del sprite
        self.rectangulo_personaje.width = width
        self.rectangulo_personaje.height = height
        self.vida = 20  # Vida inicial del enemigo
        self.cantidad_daño_personaje = cantidad_daño_personaje
        self.cantidad_daño_proyectil = cantidad_daño_proyectil
        self.vivo = True
        

    def actualizar(self, personaje, lista_proyectiles,PANTALLA):
        if self.rango_movimiento is not None:
            if self.rectangulo_personaje.x >= self.rango_movimiento[1]:
                self.direccion = -1  # Cambiar la dirección si llega al límite derecho
                self.lista_animaciones = self.lista_animaciones_izquierda
            elif self.rectangulo_personaje.x <= self.rango_movimiento[0]:
                self.direccion = 1  # Cambiar la dirección si llega al límite izquierdo
                self.lista_animaciones = self.lista_animaciones_derecha

            self.rectangulo_personaje.x += self.velocidad * self.direccion
            self.rectangulo_personaje.y = self.y_inicial  # Mantener la posición vertical constante

            if personaje.rectangulo_personaje.colliderect(self.rectangulo_personaje):
                self.recibir_daño(self.cantidad_daño_personaje,PANTALLA,personaje)  

    # Verificar colisión entre proyectiles y enemigo
            for proyectil in lista_proyectiles:
                if proyectil.rect.colliderect(self.rectangulo_personaje):
                    self.recibir_daño(self.cantidad_daño_proyectil,PANTALLA,personaje)  


    #def animar_enemigo(self, PANTALLA):
     #   if self.direccion == 1:
     #       self.animar_personaje(self.lista_animaciones_derecha, PANTALLA)
      #  else:
      #      self.animar_personaje(self.lista_animaciones_izquierda, PANTALLA)

    

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

    #def morir(self, pantalla):
        #Lógica para el enemigo al morir
            #self.velocidad = 5  # Velocidad de caída del enemigo
            #self.direccion = 1  # Dirección de caída (hacia abajo)
            #self.lista_animaciones = self.lista_animaciones_derecha  # Animaciones de caída
            #self.vivo = False
            # Voltear el sprite 180 grados
            #self.lista_animaciones_derecha[0] = pygame.transform.flip(self.lista_animaciones_derecha[0], True, False)

            #while self.rectangulo_personaje.y < pantalla.get_height():
                   # self.rectangulo_personaje.y += self.velocidad
                    #Mostrar la animación de caída del enemigo
                    #self.animar_personaje(self.lista_animaciones, pantalla)

        # Eliminar el enemigo de la lista de sprites
    
   
    def morir(self, pantalla,personaje):
    # Lógica para el enemigo al morir
        self.velocidad = 5  # Velocidad de caída del enemigo
        self.direccion = 1  # Dirección de caída (hacia abajo)
        self.vivo = False
        personaje.puntos += 10

        # Cambiar las animaciones a gusano_muerto
        self.lista_animaciones = self.lista_animaciones_muerte

        while self.rectangulo_personaje.y < pantalla.get_height():
            self.rectangulo_personaje.y += self.velocidad

            # Renderizar el enemigo en la nueva posición
            self.renderizar(pantalla)
            sonido_muerte.play()
            
        # Eliminar el enemigo de la lista de sprites
        self.rectangulo_personaje.y = pantalla.get_height() + self.rectangulo_personaje.height

      
        
           
