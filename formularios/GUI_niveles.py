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
from BOSS import Boss
import sys
import time
class Formulario_niveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=False):
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



    def update(self, lista_eventos, keys, screen, w):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos, keys, self.screen, w)
                if self.miNivel:
                    self.miNivel.leer_input(keys, self.screen, 1200)
                    if self.miNivel.todos_enemigos_derrotados():
                        self.avanzar_al_siguiente_nivel()
        else:
            self.hijo.update(lista_eventos, keys, screen, w)

    def avanzar_al_siguiente_nivel(self):
        if self.miNivel.nivel_actual == 0:
            self.mostrar_cinematica_2([],self.screen,1200)
            self.btn_LV2_click([], self.screen, 1200)
            self.miNivel.nivel_actual +=1
        elif self.miNivel.nivel_actual == 1:
            self.mostrar_cinematica_3({},self.screen, 1200)
            self.btn_LVBOSS_click([], self.screen, 1200)
            self.miNivel.nivel_actual = 2
        elif self.miNivel.nivel_actual == 2:
            self.mostrar_cinematica([], self.screen, 1200)
             
            # Aquí debes agregar la lógica correspondiente según tus necesidades
        else:    # Por ejemplo, puedes mostrar un mensaje de "Juego completado" o reiniciar el juego
            print("¡Juego completado!")
        
           

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
        gusano_enemigo_3 = Enemigo(889,270, 0, 5, [gusano, gusano_izquierda], (805, 950), 40, 35, 10, 5)
        gusano_enemigo_2 = Enemigo(581, 90, 0, 5, [gusano, gusano_izquierda], (502, 789), 40, 35, 10, 5)
        gusano_enemigo = Enemigo(189, 275, 0, 5, [gusano, gusano_izquierda], (102, 296), 40, 35, 10, 5)
        
        
        lista_proyectiles = []

        proyectiles = pygame.sprite.Group()


        planta_enemigo = PlantaEnemigo(300,450,0,0,0,lista_animaciones_planta,50,50,10, 5,220)
        planta_enemigo_2 = PlantaEnemigo(550,450,0,0,0,lista_animaciones_planta,50,50,10, 5,200)

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
        plataforma_4 = Plataforma(410,420,0,(100,75),2)
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
                   personaje_ataque_izquierda,personaje_muerto],20,20)
        lista_enemigos=[]
        troll_1 = Enemigo(189, 260, 0, 5, [troll_derecha, troll], (102, 296), 40, 45, 10, 5)
        troll_2 = Enemigo(581, 80, 0, 5, [troll_derecha, troll], (502, 789), 40, 45, 10, 5)
        troll_3 = Enemigo(889,260, 0, 5, [troll_derecha, troll], (805, 950), 40, 45, 10, 5)
        troll_4 = Enemigo(400,380, 0, 5, [troll_derecha, troll], (400, 450), 40, 45, 10, 5)
        
        lista_proyectiles = []

        proyectiles = pygame.sprite.Group()


        planta_enemigo = PlantaEnemigo(300,450,0,0,0,lista_animaciones_planta,50,50,10, 5,220)
        planta_enemigo_2 = PlantaEnemigo(550,450,0,0,0,lista_animaciones_planta,50,50,10, 5,200)
        planta_enemigo_3 = PlantaEnemigo(582,82,0,0,0,lista_animaciones_planta,50,50,10, 5,200)

        lista_enemigos.extend([troll_1,troll_2,troll_3,planta_enemigo,planta_enemigo_2,troll_4,planta_enemigo_3])

        #items////////////

        estrella = Item(889,200, "estrella")
        estrella_2 = Item(581,80, "estrella")
        estrella_3 = Item(185,270, "estrella")
        estrella_4 = Item(285,500, "estrella")
        lista_estrellas = [estrella, estrella_2, estrella_3,estrella_4]

        corazon_1 = Item(300,100, "corazon")
        corazon_2 = Item(500,80, "corazon")
        corazon_3 = Item(100,270, "corazon")
        corazon_4 = Item(300,480, "corazon")

        lista_corazones = [corazon_1,corazon_2,corazon_3,corazon_4]
        self.miNivel = Nivel(self.screen,personaje,plataformas,"./mapa/mapa_1.jpg",lista_enemigos,lista_proyectiles,lista_estrellas,lista_corazones,1200,1)
        self.miNivel.generarNivel("mapa\mapa_2.png")
        

    def btn_LVBOSS_click(self,keys,PANTALLA,W):
        
        plataforma = Plataforma(100,300,0,(200,75),0)
        plataforma_2 = Plataforma(800,300,0,(200,75),0)
        plataforma_3 = Plataforma(500,120,0,(300,75),2)
        plataforma_4 = Plataforma(410,420,0,(100,75),2)
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
                   personaje_ataque_izquierda,personaje_muerto],20,20)
        lista_enemigos=[]
        gusano_enemigo_3 = Enemigo(889,270, 0, 5, [troll_derecha, troll], (805, 950), 40, 45, 10, 5)
        gusano_enemigo_2 = Enemigo(581, 90, 0, 5, [troll_derecha, troll], (502, 789), 40, 45, 10, 5)
        gusano_enemigo = Enemigo(189, 270, 0, 5, [troll_derecha, troll], (102, 296), 40, 45, 10, 5)
        troll_4 = Enemigo(400,390, 0, 5, [troll_derecha, troll], (400, 450), 40, 45, 10, 5)
        BOSS = Boss(400,100,0,(30,350),6,[boss,boss_daño],200,225,10,100,700)
        lista_proyectiles = []

        proyectiles = pygame.sprite.Group()


        
        lista_enemigos.extend([gusano_enemigo,gusano_enemigo_2,gusano_enemigo_3,troll_4,BOSS])

        #items////////////

        estrella = Item(889,200, "estrella")
        estrella_2 = Item(581,80, "estrella")
        estrella_3 = Item(185,270, "estrella")
        estrella_4 = Item(285,500, "estrella")
        lista_estrellas = [estrella, estrella_2, estrella_3,estrella_4]

        corazon_1 = Item(300,100, "corazon")
        corazon_2 = Item(500,80, "corazon")
        corazon_3 = Item(100,270, "corazon")
        corazon_4 = Item(300,480, "corazon")


        
        lista_corazones = [corazon_1,corazon_2,corazon_3,corazon_4]
        self.miNivel = Nivel(self.screen,personaje,plataformas,"./mapa/mapa_1.jpg",lista_enemigos,lista_proyectiles,lista_estrellas,lista_corazones,1200,2)
        self.miNivel.nivel_boss = True
        self.miNivel.generarNivel("mapa\mapa_3n.png")  


    def mostrar_cinematica(self,keys,PANTALLA,W):
        # Reproducir la cinemática
        #pantalla_cinematica = pygame.display.set_mode((800, 600))  # Crear una nueva ventana para la cinemática
        fondo_cinematica = pygame.image.load("formularios\cosas_formularios/fondo_formulario.png")
        imagen_1 = pygame.image.load("cinematicas\cinematica_heroe.png")
        imagen_2 = pygame.image.load("cinematicas\poly.jpeg")
        imagen_2=pygame.transform.scale(imagen_2, (300, 300))
        texto = "¡El jefe ha sido derrotado!,\nGracias Por Tu Ayuda Mi Perra, Poly Esta Bien .\n Gracias Por Jugar"
        fuente = pygame.font.SysFont("Arial", 40)

        PANTALLA.blit(fondo_cinematica, (0, 0))
        PANTALLA.blit(imagen_1, (100, 100))
        PANTALLA.blit(imagen_2, (500, 100))
        PANTALLA.blit(fuente.render(texto, True, (255, 255, 255)), (50,400))
        pygame.display.flip()

        # Pausa para mostrar la cinemática
        time.sleep(5)

        # Continuar con el juego
        #self.avanzar_al_siguiente_nivel()

    def mostrar_cinematica_2(self, keys, PANTALLA, W):
        # Reproducir la cinemática
        fondo_cinematica = pygame.image.load("mapa/mapa_2.png")
        factor_escala = 1.2  # Factor de escala para aumentar el ancho
        nuevo_ancho = int(W * factor_escala)  # Calcular el nuevo ancho basado en el factor de escala
        nuevo_alto = PANTALLA.get_height()  # Mantener el mismo alto
        fondo_cinematica = pygame.transform.scale(fondo_cinematica, (nuevo_ancho, nuevo_alto))
        imagen_1 = pygame.image.load("cinematicas/cinematica_heroe.png")
        imagen_1=pygame.transform.scale(imagen_1, (200, 200))
        texto = "Sigues En Busqueda De Tu Amiga Perruna, Te Acercas Al Bosque De La Araña"
        fuente = pygame.font.SysFont("Arial", 30)

        PANTALLA.blit(fondo_cinematica, (0, 0))
        PANTALLA.blit(imagen_1, (100, 30))
        PANTALLA.blit(fuente.render(texto, True, (255, 255, 255)), (60, 300))
        pygame.display.flip()

        # Pausa para mostrar la cinemática
        pygame.time.delay(3000)

        # Continuar con el juego
        self.btn_LV2_click(keys, PANTALLA, W)



    def mostrar_cinematica_3(self, keys, PANTALLA, W):
        # Reproducir la cinemática
        fondo_cinematica = pygame.image.load("mapa\mapa_3.jpg")
        factor_escala = 1.2  # Factor de escala para aumentar el ancho
        nuevo_ancho = int(W * factor_escala)  # Calcular el nuevo ancho basado en el factor de escala
        nuevo_alto = PANTALLA.get_height()  # Mantener el mismo alto
        fondo_cinematica = pygame.transform.scale(fondo_cinematica, (nuevo_ancho, nuevo_alto))
        imagen_1 = pygame.image.load("cinematicas/cinematica_heroe.png")
        imagen_1=pygame.transform.scale(imagen_1, (200, 200))
        texto = " Te Adentras En El Bosque De La Araña,\nTu ira Por Recuperar A Tu Amiga Hace Que Desbloques Tu Poder Al Maximo,\nAhora Puedes Disparar Sin Limites "
        fuente = pygame.font.SysFont("Arial", 30)

        PANTALLA.blit(fondo_cinematica, (0, 0))
        PANTALLA.blit(imagen_1, (100, 30))
        PANTALLA.blit(fuente.render(texto, True, (255, 255, 255)), (60, 300))
        pygame.display.flip()

        # Pausa para mostrar la cinemática
        pygame.time.delay(3000)

        # Continuar con el juego
        self.btn_LVBOSS_click(keys, self.screen, 1200)        