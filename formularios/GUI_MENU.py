import pygame
import sys
from pygame.locals import *


class FormularioMenu:
    def __init__(self, screen):
        self.screen = screen
        self.fondo = pygame.image.load("ruta_al_fondo.png")
        self.boton1 = pygame.image.load("ruta_al_boton1.png")
        self.boton2 = pygame.image.load("ruta_al_boton2.png")
        self.boton3 = pygame.image.load("ruta_al_boton3.png")
        self.rect_boton1 = self.boton1.get_rect(topleft=(100, 100))
        self.rect_boton2 = self.boton2.get_rect(topleft=(100, 200))
        self.rect_boton3 = self.boton3.get_rect(topleft=(100, 300))

    def actualizar(self):
        self.screen.blit(self.fondo, (0, 0))
        self.screen.blit(self.boton1, self.rect_boton1)
        self.screen.blit(self.boton2, self.rect_boton2)
        self.screen.blit(self.boton3, self.rect_boton3)

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.rect_boton1.collidepoint(evento.pos):
                    # Acción al hacer clic en el botón 1 (por ejemplo, mostrar otro formulario)
                    otro_formulario = FormularioOtro(self.screen)
                    otro_formulario.ejecutar()
                elif self.rect_boton2.collidepoint(evento.pos):
                    # Acción al hacer clic en el botón 2
                    pass
                elif self.rect_boton3.collidepoint(evento.pos):
                    # Acción al hacer clic en el botón 3
                    pass