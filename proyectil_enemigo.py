import pygame

class Proyectil_enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        super().__init__()
        self.imagenes = [
            pygame.image.load("juego_parcial/ataque_planta/1.png"),
            pygame.image.load("juego_parcial/ataque_planta/2.png"),
            pygame.image.load("juego_parcial/ataque_planta/3.png"),
            pygame.image.load("juego_parcial/ataque_planta/4.png")
        ]
        self.indice_animacion = 0
        self.image = self.imagenes[self.indice_animacion]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = velocidad

    def update(self):
        self.rect.x += self.velocidad
        self.actualizar_animacion()
        

    def actualizar_animacion(self):
        self.indice_animacion += 1
        if self.indice_animacion >= len(self.imagenes):
            self.indice_animacion = 0
        self.image = self.imagenes[self.indice_animacion]