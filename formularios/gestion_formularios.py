import pygame
import sys
from formularios.formulario_carga import Formulario_main
from formularios.GUI_OPCIONES import Formulario_opciones
from formularios.GUI_menu_score import From_menu_score
from formularios.GUI_niveles import Formulario_niveles
class Gestion_formulario():
    def __init__(self, pantalla,):
        self.formulario_main = Formulario_main(pantalla, 200, 20, 900,600, "formularios\cosas_formularios/tabla_score.png", "White", 3, True)
        self.formulario_opciones=Formulario_opciones(pantalla,200, 20, 900, 550,"White","Black",-1,True)
        self.formulario_niveles =Formulario_niveles(pantalla,200, 20, 900, 550,"White","Black",-1,True)
        self.menus_score =From_menu_score(pantalla,250,25,500,550,(220,0,220),"white",True,
                                      "formularios\cosas_formularios/tabla_score.png",0,100,10,10)
        self.pantalla = pantalla
        self.imagen_fondo = pygame.image.load("formularios/cosas_formularios/fondo_formulario.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (1200, 600))
        self.render()
    def gestionar_formulario(self,keys,eventos):

        if self.formulario_main.active:
            self.formulario_main.update(eventos,keys,1200)

    def render(self):
        self.pantalla.blit(self.imagen_fondo, (0, 0))        
            
    