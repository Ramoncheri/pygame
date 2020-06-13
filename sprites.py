import pygame as pg
from pygame.locals import *
import sys, random

BGColor= (0,0,0)
YELLOW= (255, 255, 0)
WHITE= (255, 255, 255)

class Ball(pg.sprite.Sprite):
    vx = 0
    vy = 0
    num_sprites = 12
   

    def __init__(self):
        self.image= pg.Surface((20, 20), pg.SRCALPHA, 32)  #SCRALPHA es que soporte  transparencia. El numero son los bits de color
        self.rect= self.image.get_rect()  #obtiene el rectangulo que se necesita en los sprites
        self.images= self.loadImages()
        self.image_activa = 0
        self.image.blit(self.images[self.image_activa],(0, 0))  #posiciona la imagen activa sobre el Surface image, en la coord.(0,0) del Surface
        self.reset()
        self.ping= pg.mixer.Sound('./resources/sounds/ping.wav')
        self.lost_point= pg.mixer.Sound('./resources/sounds/lost-point.wav')

    def loadImages(self):
        '''
        images= []
        for i in range (self.num_sprites):
            image= pg.image.load('./resources/sprites/f_{}.png'.format(i))
            images.append(image)
        return images
        '''
        images= [pg.image.load('./resources/sprites/f_{}.png'.format(i)) for i in range (self.num_sprites)]
        return images

    def reset(self):
        self.vx= random.choice([-2, -1, 1.3, 2]) #velocidad de la bola en  x e y
        self.vy= random.choice([-3, -1.3, 1.3, 3])
        self.rect.centerx= 400   #rect tiene los metodos para calcular el centro del rectangulo.
        self.rect.centery= 300

    def comprobarChoque(self, algo ): #el algo será el player1 y el player2
        dx= abs(self.rect.centerx - algo.rect.centerx)
        dy= abs (self.rect.centery - algo.rect.centery)

        if dx < (self.rect.w + algo.rect.w)//2 and dy < (self.rect.h + algo.rect.h)//2:
            self.vx *= - 1.1
            self.vy *= random.choice([-1.3, 0.9,  1.3])

            self.rect.centerx += self.vx
            self.rect.centery += self.vy
            self.ping.play()

    def update(self, limSupX, limSupY):
        if self.rect.centerx >= limSupX or self.rect.centerx <= 0:
            self.vx = 0
            self.vy = 0
            self.lost_point.play()
            
        if self.rect.centery >= limSupY or self.rect.centery <= 0:
            self.vy *= -1
            self.ping.play()

        self.rect.centerx += self.vx
        self.rect.centery += self.vy

        #animacion de la bola
        '''
        self.image_activa += 1
        if self.image_activa >= self.num_sprites:
            self.image_activa = 0
        '''
            #es lo mismo que:
        '''
        self.image_activa += 1
        self.image_activa = self.image_activa % self.num_sprites
        '''
            #es lo mismo que:
        self.image_activa= (self.image_activa + 1) % self.num_sprites

        self.image.blit(self.images[self.image_activa], (0, 0))


class Raquet(pg.sprite.Sprite):
    vx= 0
    vy= 0
    __color= WHITE

    def __init__(self, centerx):
        self.image= pg.Surface((20 ,100))
        self.image.fill(self.__color)
        self.rect= self.image.get_rect()
        self.rect.centerx= centerx
        self.rect.centery= 300


    @property   #como para cambiar el color, se hace a traves de una funcion(.fill), hay que hacer una funcion para cambiar el color facilmente
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, tupla_color):
        self.__color= tupla_color
        self.image.fill(self.__color)

    def update(self, limSupY):
        self.rect.centerx += self.vx
        self.rect.centery += self.vy

        if self.rect.centery > limSupY - self.rect.h//2:
            self.rect.centery = limSupY-self.rect.h//2
        if self.rect.centery <  self.rect.h //2:
            self.rect.centery = self.rect.h //2




