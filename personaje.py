import pygame
from animaciones import*

#sonido_muerte_planta = pygame.mixer.Sound('juego_parcial\SE_KeeseSwarm_Attack.wav')

class Personaje():
    def __init__(self,x_inicial,y_inicial,posicion_inicial,velocidad,lista_animaciones,cantidad_daño_personaje,cantidad_daño_proyectil,personaje_daño):

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
        self.imagen_corazon = pygame.image.load("juego_parcial/vida_estrellas/0.png")
        self.cantidad_daño_personaje = cantidad_daño_personaje
        self.cantidad_daño_proyectil = cantidad_daño_proyectil
        self.personaje_daño = personaje_daño
        self.sprites_corazones = []  # Lista para almacenar las imágenes de los corazones
        self.cargar_sprites_corazones()  


    def cargar_sprites_corazones(self):
        self.sprites_corazones = []  # Reiniciar la lista de sprites de corazones
        imagen_corazon = pygame.image.load("juego_parcial/vida_estrellas/0.png")

        for _ in range(self.vidas):
            self.sprites_corazones.append(imagen_corazon.copy())



    def vida_personaje(self, pantalla):
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
            
        
    def recibir_daño_heroe(self, cantidad, lista_enemigos, lista_proyectiles_enemigo):
        for enemigo in lista_enemigos:
            if self.rectangulo_personaje.colliderect(enemigo.rectangulo_enemigo):
                self.vida_heroe -= cantidad
                # Resto de la lógica cuando el personaje recibe daño de un enemigo
                self.cambiar_animacion_recibir_daño()
        for proyectil in lista_proyectiles_enemigo:
            if self.rectangulo_personaje.colliderect(proyectil.rect):
                self.vida_heroe -= cantidad
                self.cambiar_animacion_recibir_daño()
                lista_proyectiles_enemigo.remove(proyectil)
    def morir_heroe(self, pantalla,personaje):
    # Lógica para el enemigo al morir
        self.heroe_vivo = False
        



    
    def cambiar_animacion_recibir_daño(self):
        animacion_recibir_daño = self.personaje_daño

        if self.contador_pasos < len(self.lista_animaciones) and self.contador_pasos < len(animacion_recibir_daño):
            # Reemplazar la animación actual con la animación de recibir daño
            self.lista_animaciones = animacion_recibir_daño[:]
        else:
            # Si el contador de pasos excede el índice máximo de la lista, simplemente se reinicia
            self.contador_pasos = 0


    def aumentar_vida(self, cantidad):
        self.vida_heroe += cantidad