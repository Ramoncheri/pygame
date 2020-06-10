import pygame as pg
from pygame.locals import *
import sys

BGColor= (0,0,0)
YELLOW= (255, 255, 0)

class Ball:
    def __init__(self):
        self.vx= 2  #veloc. de x e y
        self.vy= 2
        self.x= 400
        self.y= 300
        self.w= 20  #ancho de la bola
        self.h= 20   # alto de la bola

        self.image= pg.Surface((self.w, self.h))
        self.image.fill(YELLOW)
        
    @property
    def posX(self):
        return  self.x- self.w//2   # coordenada X para situar la bola en el centro de la pantalla
        
    @property
    def posY(self):
        return self.y- self.h//2

    def move(self, limitSuperX, limitSuperY):
        if self.x >= limitSuperX or self.x <= 0:
            self.vx *= -1
            
        if self.y >= limitSuperY or self.y <= 0:
            self.vy *= -1

        self.x += self.vx
        self.y += self.vy

class Raquet:
    def __init__(self, xR):
        self.vrx= 0
        self.vry= 0
        self.wr= 20  #ancho raqueta
        self.hr= 100  #alto raqueta
        self.xr= xR    #coordenada para calcular la posicion inicial x de la raqueta
        self.yr= 300  # coordenadas para calcular la posicion inicial y de la raqueta

        self.image= pg.Surface((self.wr, self.hr))
        self.image.fill((255, 255, 255))

    @property
    def posX(self):
        return  self.xr- self.wr//2   # coordenada X para situar la raqueta en el centro de la pantalla
        
    @property
    def posY(self):
        return self.yr- self.hr//2    # devuelve el centro de la raqueta

    def raquet_move(self, limitSuperX, limitSuperY):
        self.xr += self.vrx
        self.yr += self.vry

        if self.yr >= limitSuperY - self.hr//2:
            self.yr = limitSuperY-self.hr//2
        if self.yr <=  self.hr//2:
            self.yr = self.hr//2

        




class Game:

    def __init__(self):
        pg.display.set_caption('Pong')
        self.pantalla= pg.display.set_mode((800, 600))
        self.pantalla.fill(BGColor)
        self.fondo= pg.image.load('./resources/fondo.jpg')
         
        self.ball= Ball()

        self.playerOne= Raquet(30)
        self.playerTwo = Raquet(770)



    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():   #EVENTOS
                if event.type== pg.QUIT:
                    game_over= True
                '''
                if event.type == KEYDOWN:
                    if event.key== K_w:
                        self.playerOne.vry = -5
                    
                    if event.key== K_z:
                        self.playerOne.vry = 5
                '''
            key_pressed= pg.key.get_pressed()
            if key_pressed[K_w]:
                self.playerOne.vry = -5
            elif key_pressed[K_z]:
                self.playerOne.vry = 5
            else:
                self.playerOne.vry = 0

            if key_pressed[K_UP]:
                self.playerTwo.vry = -5
            elif key_pressed[K_DOWN]:
                self.playerTwo.vry = 5
            else:
                self.playerTwo.vry = 0


            
            
            
            
            self.pantalla.blit(self.fondo, (0, 0))
            self.pantalla.blit(self.ball.image, (self.ball.posX, self.ball.posY))
            self.pantalla.blit(self.playerOne.image, (self.playerOne.posX, self.playerOne.posY))
            self.pantalla.blit(self.playerTwo.image, (self.playerTwo.posX, self.playerTwo.posY))
            self.ball.move(800, 600)
            self.playerOne.raquet_move(800, 600)
            self.playerTwo.raquet_move(800, 600)
            
            
            pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()


if __name__== '__main__':
    pg.init()
    game= Game()
    game.main_loop()
    game.quit()

