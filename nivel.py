import pygame
import sys
from animaciones import *
from pygame.locals import *
from modo_programador import *
from proyectiles import *
from personaje import Personaje
from plataforma import Plataforma
from enemigo import Enemigo
from animacion_enemigo import *

import pygame.mixer

pygame.mixer.init()
sonido_muerte = pygame.mixer.Sound('juego_parcial\Squirrel_Vo_Wait4.wav')

class Nivel1:
    def __init__(self):
        pygame.init()
        self.W, self.H = 1000, 700
        self.TAMAÑO_PANTALLA = (self.W, self.H)
        self.FPS = 15
        self.clock = pygame.time.Clock()
        self.PANTALLA = pygame.display.set_mode(self.TAMAÑO_PANTALLA)
        self.fondo_pantalla = pygame.image.load("juego_parcial/mapa/mapa_1.jpg")
        self.fondo_escalado = pygame.transform.scale(self.fondo_pantalla, self.TAMAÑO_PANTALLA)
        self.COLOR_NEGRO = (0, 0, 0)
        self.COLOR_FONDO = self.COLOR_NEGRO
        self.mirando_izquierda = False
        self.plataforma = Plataforma(100, 300, 0, (200, 75), 0)
        self.plataforma_2 = Plataforma(800, 300, 0, (200, 75), 0)
        self.plataforma_3 = Plataforma(500, 120, 0, (300, 75), 2)
        self.plataformas = [self.plataforma, self.plataforma_2, self.plataforma_3]
        self.gravedad = 1
        self.potencia_salto = -20
        self.limite_velociad_caida = 15
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.personaje = Personaje(self.H / 2 - 300, 450, 0, 10, [personaje_camina,
                                                                   personaje_quieto,
                                                                   personaje_salta,
                                                                   personaje_cae_salto,
                                                                   personaje_ataque,
                                                                   personaje_daño,
                                                                   personaje_camina_izquierda,
                                                                   personaje_quieto_izquierda,
                                                                   personaje_salta_izquierda,
                                                                   personaje_ataque_izquierda])
        self.gusano_enemigo_3 = Enemigo(889, 270, 0, 5, [gusano, gusano_izquierda], (30, 35), 805, 950, 10, 5)
        self.gusano_enemigo_2 = Enemigo(581, 90, 0, 5, [gusano, gusano_izquierda], (30, 35), 502, 789, 10, 5)
        self.gusano_enemigo = Enemigo(189, 275, 0, 5, [gusano, gusano_izquierda], (30, 35), 102, 296, 10, 5)
        self.enemigos = [self.gusano_enemigo, self.gusano_enemigo_2, self.gusano_enemigo_3]
        self.proyectiles = []
        self.en_juego = True

    def colisiones(self):
        # Colisión del personaje con las plataformas
        for plataforma in self.plataformas:
            if pygame.sprite.collide_rect(self.personaje, plataforma):
                if self.personaje.rectangulo_personaje.y < plataforma.rectangulo_plataforma.y:
                    self.personaje.rectangulo_personaje.y = plataforma.rectangulo_plataforma.y - \
                                                             self.personaje.rectangulo_personaje.height
                    self.personaje.desplazamiento_y = 0
                    self.personaje.esta_saltando = False
                elif self.personaje.rectangulo_personaje.y > plataforma.rectangulo_plataforma.y:
                    self.personaje.rectangulo_personaje.y = plataforma.rectangulo_plataforma.y + \
                                                             plataforma.rectangulo_plataforma.height
                    self.personaje.desplazamiento_y = 0

        # Colisión de los enemigos con las plataformas
        for enemigo in self.enemigos:
            for plataforma in self.plataformas:
                if pygame.sprite.collide_rect(enemigo, plataforma):
                    if enemigo.rectangulo_personaje.y < plataforma.rectangulo_plataforma.y:
                        enemigo.rectangulo_personaje.y = plataforma.rectangulo_plataforma.y - \
                                                         enemigo.rectangulo_personaje.height
                        enemigo.direccion *= -1  # Invertir la dirección del enemigo
                    elif enemigo.rectangulo_personaje.y > plataforma.rectangulo_plataforma.y:
                        enemigo.rectangulo_personaje.y = plataforma.rectangulo_plataforma.y + \
                                                         plataforma.rectangulo_plataforma.height
                        enemigo.direccion *= -1  # Invertir la dirección del enemigo

    def manejar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.en_juego = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.personaje.esta_saltando:
                        self.personaje.esta_saltando = True
                        self.personaje.desplazamiento_y = self.potencia_salto

                if event.key == pygame.K_RETURN:
                    if self.personaje.mirando_izquierda:
                        self.personaje.disparar_proyectil(self.proyectiles, -10)
                    else:
                        self.personaje.disparar_proyectil(self.proyectiles, 10)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.personaje.mover_izquierda()
        elif keys[pygame.K_RIGHT]:
            self.personaje.mover_derecha()
        else:
            self.personaje.quieto()

    def actualizar(self):
        self.personaje.actualizar(self.PANTALLA)
        self.colisiones()

        # Actualizar los enemigos
        for enemigo in self.enemigos:
            enemigo.actualizar(self.personaje, self.proyectiles, self.PANTALLA)

        # Actualizar los proyectiles
        for proyectil in self.proyectiles:
            proyectil.actualizar()
            if proyectil.rect.x < 0 or proyectil.rect.x > self.W:
                self.proyectiles.remove(proyectil)

    def renderizar(self):
        self.PANTALLA.fill(self.COLOR_FONDO)
        self.PANTALLA.blit(self.fondo_escalado, (0, 0))

        # Renderizar las plataformas
        for plataforma in self.plataformas:
            plataforma.renderizar(self.PANTALLA)

        # Renderizar los enemigos
        for enemigo in self.enemigos:
            enemigo.renderizar(self.PANTALLA)

        # Renderizar los proyectiles
        for proyectil in self.proyectiles:
            proyectil.renderizar(self.PANTALLA)

        # Renderizar el personaje
        self.personaje.renderizar(self.PANTALLA)

        pygame.display.update()

    def ejecutar_juego(self):
        while self.en_juego:
            self.clock.tick(self.FPS)
            self.manejar_eventos()
            self.actualizar()
            self.renderizar()

        pygame.quit()


nivel1 = Nivel1()
nivel1.ejecutar_juego()


