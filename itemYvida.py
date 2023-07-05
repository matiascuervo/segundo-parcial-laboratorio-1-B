import pygame


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y,tipo):
        super().__init__()
        self.imagenes_corazones = [
            pygame.image.load("./vida_estrellas\corazon_0.png"),
            pygame.image.load("./vida_estrellas/corazon_1.png"),
            pygame.image.load("./vida_estrellas/corazon_2.png"),
            pygame.image.load("./vida_estrellas/corazon_3.png"),
            pygame.image.load("./vida_estrellas/corazon_4.png")
        ]
        self.imagenes_estrellas = [
            pygame.image.load("./vida_estrellas\estrella_0.png"),
            pygame.image.load("./vida_estrellas/estrella_1.png")
        ]

        self.indice_animacion = 0
        self.image = self.imagenes_corazones[self.indice_animacion]
        self.rectangulo_item = self.image.get_rect()
        self.rectangulo_item.x = x
        self.rectangulo_item.y = y
        self.tipo = tipo
        self.contador_estrellas = 0

    def update(self):
        self.actualizar_animacion()

    def actualizar_animacion(self):
        if self.tipo == "corazon":
            self.indice_animacion += 1
            if self.indice_animacion >= len(self.imagenes_corazones):
                self.indice_animacion = 0
            self.image = self.imagenes_corazones[self.indice_animacion]
        elif self.tipo == "estrella":
            self.indice_animacion += 1
            if self.indice_animacion >= len(self.imagenes_estrellas):
                self.indice_animacion = 0
            self.image = self.imagenes_estrellas[self.indice_animacion]

    def renderizar_item(self, pantalla):
        pantalla.blit(self.image,self.rectangulo_item)

    def colision_personaje_items(self, rectangulo_personaje, vida_heroe):
        
        nueva_vida_heroe = vida_heroe

        if self.tipo == "estrella" and self.rectangulo_item.colliderect(rectangulo_personaje):
            self.contador_estrellas += 1
            print("es la estrella de items")
        if self.tipo == "corazon" and self.rectangulo_item.colliderect(rectangulo_personaje):
            nueva_vida_heroe += 100

        return nueva_vida_heroe


    def set_position(self, x, y):
        self.rectangulo_item.x = x
        self.rectangulo_item.y = y