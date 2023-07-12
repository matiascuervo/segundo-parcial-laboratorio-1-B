import pygame
from pygame.locals import *
from formularios.GUI_widget import *
import unicodedata
from formularios.GUI_textbox import*
# Dimensiones de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Inicializar pygame
pygame.init()

# Crear la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Prueba TextBox")

# Crear el TextBox
text_box = TextBox(screen, 0, 0, 300, 200, 200, 30, GRAY, WHITE, BLACK, BLACK, 2, "Arial", 20, BLACK)

# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    
    # Actualizar el TextBox
    text_box.update(pygame.event.get(), pygame.key.get_pressed(), screen, SCREEN_WIDTH)
    
    # Renderizar
    screen.fill(WHITE)
    text_box.render()
    pygame.display.flip()
    
    # Limitar la velocidad de fotogramas
    clock.tick(30)

# Finalizar pygame
pygame.quit()