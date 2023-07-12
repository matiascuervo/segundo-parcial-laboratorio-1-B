import pygame
from pygame.locals import*
from formularios.GUI_button import Button
from formularios.GUI_slider import*
from formularios.GUI_textbox import*
from formularios.GUI_label import*
from formularios.GUI_form import*
from formularios.GUI_button_image import*
from formularios.GUI_niveles import Formulario_niveles
from formularios.formulario_carga import Formulario_main
class FormularioPausa(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active, formulario_niveles, pausa, formulario_main):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        self.screen = screen
        pygame.mixer.init()
        self.formulario_niveles = formulario_niveles
        self.formulario_main = formulario_main = Formulario_main(screen, 100, 20, 900,600, "formularios\cosas_formularios/tabla_score.png", "White", 3, True, None, None, self.formulario_niveles)
        self.imagen_fondo = pygame.image.load("formularios\cosas_formularios/tabla_score.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (w, h))
        self.formulario_niveles = self.formulario_niveles =Formulario_niveles(screen,100, 20, 900, 550,"White","Black",-1,False)
        self.pausa = pausa

        self.btn = False

        self.boton_play = Button(self._slave, x, y, 100, 100, 100, 50, "White", "Blue", self.boton_play_click, "nombre", "Pause", font="Verdana", font_size=15, font_color="Black")
        self.lable_volumen = Label(self._slave, 600, 190, 100, 50, "20%", "Arial", 15, "White", "formularios\cosas_formularios\medidor_volumen.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 300, 15, self.volumen, "Red", "White")
        #self.btn_tabla = Button_Image(self._slave, x, y, 225, 100, 50, 50, "juego_parcial/formularios/Menu_BTN.png", self.btn_home_click, "m")

        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.lable_volumen)
        self.lista_widgets.append(self.slider_volumen)
        #self.lista_widgets.append(self.btn_tabla)

        

        #pygame.mixer.music.load("juego_parcial/musica/PinkFox_-_Farewell_Memories__Full_Version_.mp3")
        #pygame.mixer.music.set_volume(self.volumen)
        #pygame.mixer.music.play(-1)


        self.btn_home = Button_Image(screen=self._slave, x=w-70, y=h-70, master_x=x, master_y=y,
                                     w=50, h=50, color_background=(255, 0, 0), color_border=(255, 0, 255),
                                     onclick=self.btn_home_click, onclick_param="", text="", font="Georgia",
                                     font_size=15, font_color=(0, 225, 0), path_image="formularios\home.png")

        self.lista_widgets.append(self.btn_home)
        self.render()

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
        
        self.formulario_main.btn_play_click(screen, w)
        self.end_dialog()
        
        #self.formulario_main.btn_play_click(screen,[],w)
        #self.pausa= False
        
        #self.formulario_niveles.active = False
        
        
          # Desactivar el formulario de pausa
        
        #if self.formulario_niveles is None:
            #self.formulario_niveles = Formulario_niveles(self.screen, 100, 20, 900, 550, "White", "Black", -1, True)
        #self.show_dialog(self.formulario_niveles)


    def render(self):
        self._slave.blit(self.imagen_fondo, (0, 0))
       

    def actualizar(self, eventos, teclas):
        pass

    def dibujar(self):
        pass


    # class GestionFormularios: 
    """  def __init__(self, pantalla):
            self.pantalla = pantalla
            self.formulario_pausa = FormularioPausa(pantalla)
            self.mostrar_pausa = False

        def mostrar_formulario_pausa(self):
            self.mostrar_pausa = True

        def ocultar_formulario_pausa(self):
            self.mostrar_pausa = False

        def gestionar_formulario(self, eventos, teclas):
            if self.mostrar_pausa:
                self.formulario_pausa.actualizar(eventos, teclas)
                self.formulario_pausa.dibujar()
            else:
                # Lógica para gestionar otros formularios en el juego


                     Dentro del bucle principal del juego:
            gestion_formularios = GestionFormularios(pantalla)

            while ejecutando_juego:
                eventos = pygame.event.get()
                teclas = pygame.key.get_pressed()

            for evento in eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_p:
                        gestion_formularios.mostrar_formulario_pausa()
            
            gestion_formularios.gestionar_formulario(eventos, teclas)"""

            # Resto de la lógica del juego"""
