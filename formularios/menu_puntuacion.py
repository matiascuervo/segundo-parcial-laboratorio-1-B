import pygame
from pygame.locals import*
from formularios.GUI_label import*
from formularios.GUI_form import*
from formularios.GUI_button_image import*

class From_menu_puntuacion(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        self.screen = screen
        pygame.mixer.init()

        self.imagen_fondo = pygame.image.load("formularios\cosas_formularios/tabla_score.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (w, h))

        
        self.lable_nombre = Label(self._slave, 150, 40, 200, 100, "Nombre", "Georgia", 20, "Black", "formularios\cosas_formularios\puntos_y_jugador.png")
        self.lable_puntaje = Label(self._slave, 470, 40, 200, 100, "Puntaje", "georgia", 20, "Black", "formularios\cosas_formularios\puntos_y_jugador.png")
        self.lable_jugador_1 = Label(self._slave, 150, 150, 200, 100, "jugador1", "georgia", 20, "Black", "formularios\cosas_formularios\puntos_y_jugador.png")
        self.lable_jugador_2 = Label(self._slave, 150, 260, 200, 100, "jugador2", "georgia", 20, "Black", "formularios\cosas_formularios\puntos_y_jugador.png")
        self.lable_jugador_3 = Label(self._slave, 150, 370, 200, 100, "jugador3", "georgia", 20, "Black", "formularios\cosas_formularios\puntos_y_jugador.png")
        self.lable_puntaje_1 = Label(self._slave, 470, 150, 200, 100, "Puntaje_1", "georgia", 20, "Black", "formularios\cosas_formularios\puntos_y_jugador.png")
        self.lable_puntaje_2 = Label(self._slave, 470, 260, 200, 100, "Puntaje_2", "georgia", 20, "Black", "formularios\cosas_formularios\puntos_y_jugador.png")
        self.lable_puntaje_3 = Label(self._slave, 470, 370, 200, 100, "Puntaje_3", "georgia", 20, "Black", "formularios\cosas_formularios\puntos_y_jugador.png")

        self.lista_widgets.append(self.lable_nombre)
        self.lista_widgets.append(self.lable_puntaje)
        self.lista_widgets.append(self.lable_jugador_1)
        self.lista_widgets.append(self.lable_jugador_2)
        self.lista_widgets.append(self.lable_jugador_3)
        self.lista_widgets.append(self.lable_puntaje_1)
        self.lista_widgets.append(self.lable_puntaje_2)
        self.lista_widgets.append(self.lable_puntaje_3)
        #self.lista_widgets.append(self.btn_tabla)

        #pygame.mixer.music.load("juego_parcial/musica/PinkFox_-_Farewell_Memories__Full_Version_.mp3")
        #pygame.mixer.music.set_volume(self.volumen)
        #pygame.mixer.music.play(-1)

        self.render()

        self.btn_home = Button_Image(screen=self._slave, x=w-70, y=h-70, master_x=x, master_y=y,
                                        w=50, h=50, color_background=(255, 0, 0), color_border=(255, 0, 255),
                                        onclick=self.btn_home_click, onclick_param="", text="", font="Georgia",
                                        font_size=15, font_color=(0, 225, 0), path_image="formularios\home.png")

        self.lista_widgets.append(self.btn_home)

    def update(self, lista_eventos,keys,screen,w):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos, keys, self.screen,w)
                
        else:
            self.hijo.update(lista_eventos, keys,screen,w)


    def render(self):
        self._slave.blit(self.imagen_fondo, (0, 0))

  

    def btn_home_click(self, screen, w, master_y):
        self.end_dialog()