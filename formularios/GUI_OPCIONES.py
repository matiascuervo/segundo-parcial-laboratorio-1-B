import pygame
from pygame.locals import*
from formularios.GUI_button import*
from formularios.GUI_slider import*
from formularios.GUI_textbox import*
from formularios.GUI_label import*
from formularios.GUI_form import*
from formularios.GUI_button_image import*
from formularios.GUI_menu_score import*


class Formulario_opciones(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        self.screen = screen
        pygame.mixer.init()

        self.imagen_fondo = pygame.image.load("formularios\cosas_formularios/tabla_score.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (w, h))

        self.boton_play = Button(self._slave, x, y, 100, 100, 100, 50, "White", "Blue", self.boton_play_click, "nombre", "Pause", font="Verdana", font_size=15, font_color="Black")
        self.lable_volumen = Label(self._slave, 650, 190, 100, 50, "20%", "Arial", 15, "White", "formularios\cosas_formularios\medidor_volumen.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 300, 15, self.volumen, "Red", "White")
        #self.btn_tabla = Button_Image(self._slave, x, y, 225, 100, 50, 50, "juego_parcial/formularios/Menu_BTN.png", self.btn_home_click, "m")
        

          
        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.lable_volumen)
        self.lista_widgets.append(self.slider_volumen)
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
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos, keys,screen,w)


    def render(self):
        self._slave.blit(self.imagen_fondo, (0, 0))

    def boton_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.boton_play._color_background = "Black"
            self.boton_play._font_color = "White"
            self.boton_play.set_text("play")
        else:
            pygame.mixer.music.unpause()
            self.boton_play._color_background = "White"
            self.boton_play._font_color = "Black"
            self.boton_play.set_text("pause")

        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.lable_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_home_click(self, screen, w, master_y):
        self.end_dialog()

