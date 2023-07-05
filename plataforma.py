
import pygame

class Plataforma():
    def __init__(self, x_inicial, y_inicial,velocidad,escala_plataforma,posicion):
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.velocidad = velocidad
        #self.posicion_inicial = posicion_inicial
        self.sprites_plataforma = [
            pygame.transform.scale(pygame.image.load("./plataformas\plataforma_tierra.png"),escala_plataforma),
            pygame.transform.scale(pygame.image.load("./plataformas/0.png"),escala_plataforma),
            pygame.transform.scale(pygame.image.load("./plataformas/1.png"),escala_plataforma),
            pygame.transform.scale(pygame.image.load("./plataformas/5.png"),escala_plataforma)
        ]
        self.posicion = posicion
        self.rectangulo_plataforma = self.sprites_plataforma[posicion].get_rect()
        self.rectangulo_plataforma.x = x_inicial
        self.rectangulo_plataforma.y = y_inicial
        


    def obtener_rectangulos(self):
        diccionario = {}

        diccionario["main"] = self.rectangulo_plataforma
        diccionario["bottom"] = pygame.Rect(self.rectangulo_plataforma.left, self.rectangulo_plataforma.bottom - 6, self.rectangulo_plataforma.width, 6)
        diccionario["right"] = pygame.Rect(self.rectangulo_plataforma.right + 2, self.rectangulo_plataforma.top, 2, self.rectangulo_plataforma.height)
        diccionario["left"] = pygame.Rect(self.rectangulo_plataforma.left, self.rectangulo_plataforma.top, 2, self.rectangulo_plataforma.height)
        diccionario["top"] = pygame.Rect(self.rectangulo_plataforma.left, self.rectangulo_plataforma.top, self.rectangulo_plataforma.width, 6)
        
        return diccionario

    
    