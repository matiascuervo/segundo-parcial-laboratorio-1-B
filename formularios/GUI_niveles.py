import pygame
from pygame.locals import*
from formularios.GUI_button import*
from formularios.GUI_slider import*
from formularios.GUI_textbox import*
from formularios.GUI_label import*
from formularios.GUI_form import*
from formularios.GUI_button_image import*
from formularios.GUI_menu_score import*
from formularios.GUI_OPCIONES import*
from clase_nivel import Nivel
from personaje import Personaje
from enemigo import Enemigo
from plataforma import Plataforma
from planta_enemigo import PlantaEnemigo
from proyectiles import Proyectil
from proyectil_enemigo import Proyectil_enemigo
from animacion_enemigo import*
from animaciones import*
from itemYvida import Item

class Formulario_niveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)


        self.imagen_fondo = pygame.image.load("formularios\cosas_formularios/tabla_score.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (w, h))
        self.screen=screen
        self.btn_LV1 = Button_Image(self._slave, x , y , 250 , 100 , 200 , 100 ,"formularios\cosas_formularios\LV1.png",self.btn_LV1_click,"m")
        self.btn_LV2 = Button_Image(self._slave, x , y , 550 , 100 , 200 , 100 ,"formularios\cosas_formularios\LV2.png",self.btn_LV2_click,"m")
        self.btn_LVBOSS = Button_Image(self._slave, x , y , 350 , 301 , 250 , 150 ,"formularios\cosas_formularios\LV_BOSS.png",self.btn_LVBOSS_click,"m")
        self.miNivel = None
        self.btn_home = Button_Image(screen=self._slave, x=w-70, y=h-70, master_x=x, master_y=y,
                                     w=50, h=50, color_background=(255, 0, 0), color_border=(255, 0, 255),
                                     onclick=self.btn_home_click, onclick_param="", text="", font="Georgia",
                                     font_size=15, font_color=(0, 225, 0), path_image="formularios\home.png")

        self.lista_widgets.append(self.btn_home)
        self.lista_widgets.append(self.btn_LV1)
        self.lista_widgets.append(self.btn_LV2)
        self.lista_widgets.append(self.btn_LVBOSS)

        self.render()



    def update(self, lista_eventos,keys,w):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos,keys,self.screen,1200)
                if self.miNivel:    
                    self.miNivel.leer_input(keys,self.screen,1200)
        else:
            self.hijo.update(lista_eventos,keys,w)

    def render(self):
        self._slave.blit(self.imagen_fondo, (0, 0))    


    def btn_home_click(self, screen, w, master_y):
        self.end_dialog()    

    def btn_LV1_click(self,keys,PANTALLA,W):
       
        plataforma = Plataforma(100,300,0,(200,75),0)
        plataforma_2 = Plataforma(800,300,0,(200,75),0)
        plataforma_3 = Plataforma(500,120,0,(300,75),2)
        plataformas=[plataforma,plataforma_2,plataforma_3]

        personaje = Personaje(50,450, 0, 10,[personaje_camina,
                   personaje_quieto,
                   personaje_salta,
                   personaje_cae_salto,
                   personaje_ataque,
                   personaje_muerte ,
                   personaje_camina_izquierda,
                   personaje_quieto_izquierda,
                   personaje_salta_izquierda,
                   personaje_ataque_izquierda],20,20)
        lista_enemigos=[]
        gusano_enemigo_3 = Enemigo(889,270, 0, 5, [gusano, gusano_izquierda], (805, 950), 30, 35, 10, 5)
        gusano_enemigo_2 = Enemigo(581, 90, 0, 5, [gusano, gusano_izquierda], (502, 789), 30, 35, 10, 5)
        gusano_enemigo = Enemigo(189, 275, 0, 5, [gusano, gusano_izquierda], (102, 296), 30, 35, 10, 5)
        
        
        lista_proyectiles = []

        proyectiles = pygame.sprite.Group()


        planta_enemigo = PlantaEnemigo(300,500,0,0,0,lista_animaciones_planta,50,50,10, 5,220)
        planta_enemigo_2 = PlantaEnemigo(550,500,0,0,0,lista_animaciones_planta,50,50,10, 5,200)

        lista_enemigos.extend([gusano_enemigo,gusano_enemigo_2,gusano_enemigo_3,planta_enemigo,planta_enemigo_2])

        #items////////////

        estrella = Item(889,200, "estrella")
        estrella_2 = Item(581,80, "estrella")
        estrella_3 = Item(185,270, "estrella")
        lista_estrellas = [estrella, estrella_2, estrella_3]

        corazon_1 = Item(300,100, "corazon")
        corazon_2 = Item(500,80, "corazon")
        corazon_3 = Item(100,270, "corazon")

        lista_corazones = [corazon_1,corazon_2,corazon_3]
        self.miNivel = Nivel(self.screen,personaje,plataformas,"./mapa/mapa_1.jpg",lista_enemigos,lista_proyectiles,lista_estrellas,lista_corazones,1200,0)
        self.miNivel.generarNivel("./mapa/mapa_1.jpg")
        
        
                

    def btn_LV2_click(self,keys,PANTALLA,W):
            
        plataforma = Plataforma(100,300,0,(200,75),0)
        plataforma_2 = Plataforma(800,300,0,(200,75),0)
        plataforma_3 = Plataforma(500,120,0,(300,75),2)
        plataforma_4 = Plataforma(400,420,0,(100,75),2)
        plataformas=[plataforma,plataforma_2,plataforma_3,plataforma_4]

        personaje = Personaje(50,450, 0, 10,[personaje_camina,
                   personaje_quieto,
                   personaje_salta,
                   personaje_cae_salto,
                   personaje_ataque,
                   personaje_muerte ,
                   personaje_camina_izquierda,
                   personaje_quieto_izquierda,
                   personaje_salta_izquierda,
                   personaje_ataque_izquierda],20,20)
        lista_enemigos=[]
        gusano_enemigo_3 = Enemigo(889,270, 0, 5, [troll_derecha, troll], (805, 950), 40, 45, 10, 5)
        gusano_enemigo_2 = Enemigo(581, 90, 0, 5, [troll_derecha, troll], (502, 789), 40, 45, 10, 5)
        gusano_enemigo = Enemigo(189, 270, 0, 5, [troll_derecha, troll], (102, 296), 40, 45, 10, 5)
        troll_4 = Enemigo(400,390, 0, 5, [troll_derecha, troll], (400, 450), 40, 45, 10, 5)
        
        lista_proyectiles = []

        proyectiles = pygame.sprite.Group()


        planta_enemigo = PlantaEnemigo(300,500,0,0,0,lista_animaciones_planta,50,50,10, 5,220)
        planta_enemigo_2 = PlantaEnemigo(550,500,0,0,0,lista_animaciones_planta,50,50,10, 5,200)

        lista_enemigos.extend([gusano_enemigo,gusano_enemigo_2,gusano_enemigo_3,planta_enemigo,planta_enemigo_2,troll_4])

        #items////////////

        estrella = Item(889,200, "estrella")
        estrella_2 = Item(581,80, "estrella")
        estrella_3 = Item(185,270, "estrella")
        lista_estrellas = [estrella, estrella_2, estrella_3]

        corazon_1 = Item(300,100, "corazon")
        corazon_2 = Item(500,80, "corazon")
        corazon_3 = Item(100,270, "corazon")

        lista_corazones = [corazon_1,corazon_2,corazon_3]
        self.miNivel = Nivel(self.screen,personaje,plataformas,"./mapa/mapa_1.jpg",lista_enemigos,lista_proyectiles,lista_estrellas,lista_corazones,1200,1)
        self.miNivel.generarNivel("mapa\mapa_2.png")
        

    def btn_LVBOSS_click(self,param):
        pass    