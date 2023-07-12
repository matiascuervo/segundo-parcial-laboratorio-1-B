import pygame

class Proyectil_enemigo_jefe(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad_x, velocidad_y):
        super().__init__()
        self.imagenes = [
            pygame.transform.scale(pygame.image.load("ataque_planta/boss_0.png"),(30,30)),
            pygame.transform.scale(pygame.image.load("ataque_planta/boss_1.png"),(30,30))
        ]
        self.indice_animacion = 0
        self.image = self.imagenes[self.indice_animacion]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        self.actualizar_animacion()

    def actualizar_animacion(self):
        self.indice_animacion += 1
        if self.indice_animacion >= len(self.imagenes):
            self.indice_animacion = 0
        self.image = self.imagenes[self.indice_animacion]