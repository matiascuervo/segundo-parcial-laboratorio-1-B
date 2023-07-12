import pygame
from pygame.locals import*
from formularios.GUI_label import*
from formularios.GUI_form import*
from formularios.GUI_button_image import*

class From_menu_score(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active,path_image,margen_y,margen_x,espacio):
        super().__init__(screen, x, y, w, h, color_background,color_border, active)

        aux_imagen =pygame.image.load(path_image)
        aux_imagen =pygame.transform.scale(aux_imagen,(w,h))

        self._slave = aux_imagen
        self._score=[{"judaor":"matias","score":"9000"},
                    {"judaor":"guido","score":"5000"},
                    {"judaor":"ivan","score":"3000"}]


        self.margen_y = margen_y
        
        label_jugador = Label(self._slave,x=margen_x + 10, y=20 , w=w/2-margen_x-10,h=50,text="jugador",
                       font="Georgia",font_size=30,font_color ="White",path_image="formularios\cosas_formularios\puntos_y_jugador.png")
        
        label_puntaje= Label(self._slave,x=margen_x + 10 + w/2-margen_x-10, y=20 , w=w/2-margen_x-10,h=50,text="puntaje",
                       font="Georgia",font_size=30,font_color ="White",path_image="formularios\cosas_formularios\puntos_y_jugador.png")
        
        lable_volumen_x = Label(self._slave, 200, 190, 100, 50, "20%", "Arial", 15, "White", "formularios\cosas_formularios\medidor_volumen.png")
        self.lista_widgets.append(label_jugador)
        self.lista_widgets.append(label_puntaje)
        self.lista_widgets.append(lable_volumen_x)

        pos_inicial_y = margen_y

        for j in self._score:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador= Label(self._slave,pos_inicial_x,pos_inicial_y,w/2-margen_x ,100,cadena,"Georgia",30,"White","formularios\cosas_formularios\puntos_y_jugador.png")
                self.lista_widgets.append(jugador)

                pos_inicial_x += w/2 - margen_x
            pos_inicial_y += 100 + espacio  


        self.btn_home = Button_Image(screen=self._slave,x= w-70, y = h-70,master_x=x, master_y= y,
                                        w=50,h=50,color_background=(255,0,0),color_border=(255,0,255),
                                        onclick = self.btn_home_click,onclick_param="",text="",font="Georgia",
                                        font_size= 15 , font_color = (0,225,0),path_image="formularios\home.png")
        
        self.lista_widgets.append(self.btn_home)
        

    def btn_home_click(self,screen, w, master_y):
        self.active = False
        self.end_dialog()
        

    def update(self, lista_eventos,keys,screen,w):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos,keys,screen,w)
            self.draw()
            
            
            
