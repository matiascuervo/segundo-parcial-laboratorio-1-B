import pygame
from pygame.locals import*
import sys
from formularios.formulario_carga import Formulario_main
from formularios.MENU_PAUSA import FormularioPausa
from formularios.GUI_OPCIONES import Formulario_opciones
from formularios.GUI_niveles import Formulario_niveles
from formularios.menu_puntuacion import From_menu_puntuacion

class Gestion_formulario():
    def __init__(self, pantalla):
        self.form_puntaje= From_menu_puntuacion(pantalla,100,25,900,550,"Red","Blue",-1,False)
        self.formulario_opciones=Formulario_opciones(pantalla,100, 20, 900, 550,"White","Black",-1,False)

        self.formulario_niveles =Formulario_niveles(pantalla,100, 20, 900, 550,"White","Black",-1,False)
        self.formulario_main = Formulario_main(pantalla, 100, 20, 900,600, "formularios\cosas_formularios/tabla_score.png", "White", 3, True, self.form_puntaje, self.formulario_opciones, self.formulario_niveles)
        
        #self.pausa = False
        self.formulario_pausa = FormularioPausa(pantalla, 200, 20, 700, 600, "formularios/cosas_formularios/tabla_score.png", "White", 3, False, self.formulario_niveles, False, self.formulario_main)
        
        self.pantalla = pantalla
        self.imagen_fondo = pygame.image.load("formularios/cosas_formularios/fondo_formulario.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (1200, 600))
        
        
        

        self.render()   
    def gestionar_formulario(self, keys, eventos):
        #print("pausa Active: " + str(self.formulario_pausa.active))
        #print("pausa Bool: " + str(self.formulario_pausa.pausa))
        #print("Main: " + str(self.formulario_main.active))
        #print("Niv: " + str(self.formulario_niveles.active))
        #print("Opc: " + str(self.formulario_opciones.active))
        #print("Score: " + str(self.form_puntaje.active))
        #print("Pausa: " + str(self.formulario_pausa.active))

        
        if keys[pygame.K_p]:
            self.formulario_pausa.pausa = not self.formulario_pausa.pausa
            self.formulario_pausa.active = not self.formulario_pausa.active
            pygame.time.wait(200)  # Esperar un tiempo para evitar la repetición rápida de teclas

        


        if self.formulario_pausa.pausa:
            self.formulario_pausa.active = True
            #self.formulario_niveles.active = True
            self.formulario_main.active = False
            #print("Ahora Form Pausa")
            self.formulario_pausa.update(eventos, keys, self.pantalla, 1200)
        elif  self.formulario_niveles.active and not self.formulario_pausa.active:
            self.formulario_niveles.update(eventos, keys, self.pantalla, 1200)
            #print("Ahora Form Niveles")
        elif self.form_puntaje.active:
            #print("Ahora Form Score")
            self.form_puntaje.update(eventos,keys, self.pantalla, 1200)
        elif self.formulario_opciones.active:
            #print("Ahora Form Opciones")
            self.formulario_opciones.update(eventos, keys, self.pantalla, 1200)
        elif self.formulario_main.active and not self.formulario_niveles.miNivel:
            #print("Ahora Form Main")
            self.formulario_main.update(eventos, keys, self.pantalla, 1200)
        else:
            self.formulario_main.update(eventos, keys, self.pantalla, 1200)
            print("DONDE ESTOY")
        
       
        


    def render(self):
        
        self.pantalla.blit(self.imagen_fondo, (0, 0))
        if self.formulario_pausa.pausa:
            self.formulario_pausa.draw()
            self.formulario_pausa.render()

        if self.formulario_niveles.active:
            self.formulario_niveles.draw()
            self.formulario_niveles.render()

        if self.form_puntaje.active:
            self.form_puntaje.draw()
            self.form_puntaje.render()

        if self.formulario_opciones.active:
            self.formulario_opciones.draw()
            self.formulario_opciones.render()

        if self.formulario_main.active and not self.formulario_niveles.miNivel:
            self.formulario_main.draw()
            self.formulario_main.render()