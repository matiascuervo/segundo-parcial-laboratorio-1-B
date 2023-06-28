import pygame

def girar_imagenes(lista,flip_x,flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return lista_girada

def rescalar_imagenes(lista_animaciones,W,H):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i],(W,H))


personaje_quieto = [
    pygame.image.load("juego_parcial/quieto/0.png"),
    pygame.image.load("juego_parcial/quieto/1.png"),
    pygame.image.load("juego_parcial/quieto/2.png")
]

personaje_camina = [
    pygame.image.load("juego_parcial/caminar/6.png"),
    pygame.image.load("juego_parcial/caminar/7.png"),
    pygame.image.load("juego_parcial/caminar/8.png"),
    pygame.image.load("juego_parcial/caminar/9.png"),
    pygame.image.load("juego_parcial/caminar/10.png"),
    pygame.image.load("juego_parcial/caminar/11.png")
]

personaje_camina_izquierda = girar_imagenes(personaje_camina,True,False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto, True,False)

personaje_salta = [
    pygame.image.load("juego_parcial/salto/18.png"),
    pygame.image.load("juego_parcial/salto/19.png"),
    pygame.image.load("juego_parcial/salto/20.png")
]

personaje_salta_izquierda = girar_imagenes(personaje_salta, True, False)

personaje_cae_salto = [
    pygame.image.load("juego_parcial/salto/24.png"),
    pygame.image.load("juego_parcial/salto/25.png"),
    pygame.image.load("juego_parcial/salto/26.png")
]

personaje_daño = [
    pygame.image.load("juego_parcial/daño/34.png"),
    pygame.image.load("juego_parcial/daño/35.png")
]

personaje_ataque = [
    pygame.image.load("juego_parcial/ataque fuerte/30.png"),
    pygame.image.load("juego_parcial/ataque fuerte/31.png"),
    pygame.image.load("juego_parcial/ataque fuerte/32.png"),
    pygame.image.load("juego_parcial/ataque fuerte/33.png")
]


personaje_ataque_izquierda=girar_imagenes(personaje_ataque,True,False)

personaje_daño=[pygame.image.load("juego_parcial\daño/34.png"),
                pygame.image.load("juego_parcial\daño/35.png"),
                pygame.image.load("juego_parcial\daño/40.png"),
                pygame.image.load("juego_parcial\daño/41.png"),
                pygame.image.load("juego_parcial\daño/muerto.png"),]


































"""class Personaje:
    def __init__(self, pos_x, pos_y, sprite_paths):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprites = []
        self.current_sprite_index = 0
        self.animation_speed = 0.2  # Velocidad de la animación (ajústala según sea necesario)

        for path in sprite_paths:
            sprite = pygame.image.load(path)
            self.sprites.append(sprite)

        self.animation_timer = 0

    def mover(self, desplazamiento_x, desplazamiento_y):
        self.pos_x += desplazamiento_x
        self.pos_y += desplazamiento_y

    def animar(self, dt):
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_sprite_index = (self.current_sprite_index + 1) % len(self.sprites)

    def dibujar(self, pantalla):
        pantalla.blit(self.sprites[self.current_sprite_index], (self.pos_x, self.pos_y))"""
