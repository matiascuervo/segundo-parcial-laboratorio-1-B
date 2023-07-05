import pygame
from pygame.locals import*
from formularios.GUI_button import Button
from formularios.GUI_slider import*
from formularios.GUI_textbox import*
from formularios.GUI_label import*
from formularios.GUI_form import*
from formularios.GUI_button_image import*
from formularios.GUI_menu_score import*
from formularios.GUI_OPCIONES import*
from formularios.GUI_niveles import*

class Formulario_main(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border ="Black", border_size = -1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.falg_play = True
        self.screen = screen
        pygame.mixer.init()

        self.imagen_fondo = pygame.image.load("formularios\cosas_formularios/tabla_score.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (w, h))
        ### controles####


        #self.txt_box = TextBox(self._slave , x , y , 50 , 50 , 150 ,30,"Grey","White","Red","Blue",2,font ="Georgia", font_size = 15, font_color = "Black" )
        #self.boton_play = Button(self._slave,x , y , 100 , 100 , 100 ,50,"White","Blue",self.boton_play_click,"nombre","Pause",font="Verdana", font_size = 15 , font_color= "Black")
        #self.lable_volumen = Label(self._slave, 650 , 190 , 100 , 50 , "20%","Arial", 15 ,"White","juego_parcial/formularios\medidor_volumen.png")
        #self.slider_volumen = Slider(self._slave, x , y , 100 , 200 , 300 , 15,self.volumen ,"Red","White")
        
        self.btn_play = Button_Image(self._slave, x , y , 350 , 201 , 200 , 100 ,"formularios\cosas_formularios/tabla_fina.png",self.btn_play_click,"m")
        self.btn_opciones = Button_Image(self._slave, x , y , 350 , 301 , 200 , 100 ,"formularios\cosas_formularios/tabla_fina.png",self.btn_opciones_click,"m")
        self.btn_tabla = Button_Image(self._slave, x , y , 350 , 401 , 200 , 100 ,"formularios\cosas_formularios/tabla_fina.png",self.btn_tabla_click,"m")
        self.lable_play = Label(self._slave, 350 , 201 , 200 , 100 , "jugar","medieval", 25 ,"Black","formularios\cosas_formularios\label_trasparrente.png")
        self.lable_opciones = Label(self._slave, 350 , 301 , 200 , 100 , "opciones","medieval", 25 ,"Black","formularios\cosas_formularios\label_trasparrente.png")
        self.lable_tabla = Label(self._slave, 350 , 401 , 200 , 100 , "pociciones","medieval", 25 ,"Black","formularios\cosas_formularios\label_trasparrente.png")
        self.lable_titulo = Label(self._slave, 212 , 51 , 500 , 100 , "El Rescate De La Poly","medieval", 25 ,"Black","formularios\cosas_formularios\puntos_y_jugador.png")
        #agregarlos###
        #self.lista_widgets.append(self.txt_box)
        #self.lista_widgets.append(self.boton_play)
        #self.lista_widgets.append(self.lable_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_opciones)
        self.lista_widgets.append(self.lable_opciones)
        self.lista_widgets.append(self.lable_play)
        self.lista_widgets.append(self.lable_tabla)
        self.lista_widgets.append(self.lable_titulo)
        pygame.mixer.music.load("musica\PinkFox_-_Farewell_Memories__Full_Version_.mp3")

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()


    def update(self, lista_eventos,keys,W):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos,keys,self.screen,W)
                #self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos,keys,W)

    def render(self):
        self._slave.blit(self.imagen_fondo, (0, 0))
        #self._slave.fill(self._color_background)  


   

    def btn_tabla_click(self,texto):
        dic_score =[{"judaor":"matias","score":"9000"},
                    {"judaor":"guido","score":"5000"},
                    {"judaor":"ivan","score":"3000"}]

        form_puntaje= From_menu_score(self._master,250,25,500,550,(220,0,220),"white",True,
                                      "formularios\cosas_formularios/tabla_score.png",dic_score,100,10,10)


        self.show_dialog(form_puntaje)   


    def btn_opciones_click(self,keys,screen,w):

        form_opciones= Formulario_opciones(self._master,200, 20, 900, 550,"White","Black",-1,True) 

        self.show_dialog(form_opciones)    


    def btn_play_click(self,texto,screen,w):

        from_niveles = Formulario_niveles(self._master,200, 20, 900, 550,"White","Black",-1,True)

        self.show_dialog(from_niveles)

        