import pygame
from animaciones import*


class Personaje():
    def __init__(self,x_inicial,y_inicial,posicion_inicial,velocidad,lista_animaciones):

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


    def animar_personaje(self,accion_personaje,PANTALLA):
        
    
        largo = len(accion_personaje)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0    

        PANTALLA.blit(accion_personaje[self.contador_pasos],self.rectangulo_personaje)
        self.contador_pasos+= 1  
              
    def obtener_rectangulos(self):
        diccionario = {}

        diccionario["main"] = self.rectangulo_personaje
        diccionario["bottom"] = pygame.Rect(self.rectangulo_personaje.left, self.rectangulo_personaje.bottom - 6, self.rectangulo_personaje.width, 6)
        diccionario["right"] = pygame.Rect(self.rectangulo_personaje.right + 2, self.rectangulo_personaje.top, 2, self.rectangulo_personaje.height)
        diccionario["left"] = pygame.Rect(self.rectangulo_personaje.left, self.rectangulo_personaje.top, 2, self.rectangulo_personaje.height)
        diccionario["top"] = pygame.Rect(self.rectangulo_personaje.left, self.rectangulo_personaje.top, self.rectangulo_personaje.width, 6)
        
        return diccionario    