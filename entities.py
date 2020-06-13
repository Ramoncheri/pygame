import pygame as pg
from pygame.locals import *
import sys, random

BGColor= (0,0,0)
YELLOW= (255, 255, 0)
WHITE= (255, 255, 255)

class Movil:
    vx= 0
    vy= 0
    __color= WHITE
    def __init__(self, w, h, centerX=0, centerY= 0):
        self.w= w
        self.h= h
        self.Cx= centerX
        self.Cy= centerY

        self.image= pg.Surface((self.w, self.h))
        self.image.fill(self.__color)

    @property
    def posX(self):
        return  self.Cx- self.w//2   # coordenada X para situar la bola en el centro de la pantalla
        
    @property
    def posY(self):
        return self.Cy- self.h//2

    @property   #como para cambiar el color, se hace a traves de una funcion(.fill), hay que hacer una funcion para cambiar el color facilmente
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, tupla_color):
        self.__color= tupla_color
        self.image.fill(self.__color)

    def move(self, limSupX, limSupY):
        pass  #permite crear objetos que no tengan movimiento. El movimiento se define en las clases hijas que si tienen movimiento

class Ball(Movil):
    def __init__(self):
        #Movil.__init(self, 20, 20)  Es lo mismo que la siguiente linea
        super().__init__(20, 20)  #la posicion del objeto la toma de la funcion reset
        self.reset()
        self.color= YELLOW
        self.ping= pg.mixer.Sound('./resources/sounds/ping.wav')
        self.lost_point= pg.mixer.Sound('./resources/sounds/lost-point.wav')
    
    def move(self, limSupX, limSupY):
    
        if self.Cx >= limSupX or self.Cx <= 0:
            self.vx = 0
            self.vy = 0
            self.lost_point.play()
            
        if self.Cy >= limSupY or self.Cy <= 0:
            self.vy *= -1
            self.ping.play()

        self.Cx += self.vx
        self.Cy += self.vy

    def reset(self):
        self.vx= random.choice([-2, -1, 1.3, 2]) #velocidad de la bola en  x e y
        self.vy= random.choice([-3, -1.3, 1.3, 3])
        self.Cx= 400
        self.Cy= 300

    def comprobarChoque(self, algo ): #el algo será el player1 y el player2
        dx= abs(self.Cx - algo.Cx)
        dy= abs (self.Cy - algo.Cy)

        if dx < (self.w + algo.w)//2 and dy < (self.h + algo.h)//2:
            self.vx *= - 1.1
            self.vy *= random.choice([-1.3, 0.9,  1.3])
            self.Cx += self.vx
            self.Cy += self.vy
            self.ping.play()

class Raquet(Movil):
    def __init__(self, centerX):
        super().__init__(20, 100, centerX, 300)

    def raquet_move(self, limSupX, limSupY):
        self.Cx += self.vx
        self.Cy += self.vy

        if self.Cy > limSupY - self.h//2:
            self.Cy = limSupY-self.h//2
        if self.Cy <  self.h //2:
            self.Cy = self.h //2