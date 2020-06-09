import pygame as pg
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

        self.image= pg.Surface((20, 20))
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


class Game:

    def __init__(self):
        pg.display.set_caption('Pong')
        self.pantalla= pg.display.set_mode((800, 600))
        self.pantalla.fill(BGColor)
        self.fondo= pg.image.load('./resources/fondo.jpg')
        
        
        self.ball= Ball()

        

    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type== pg.QUIT:
                    game_over= True

            
            self.pantalla.blit(self.fondo, (0, 0))
            self.pantalla.blit(self.ball.image, (self.ball.posX, self.ball.posY))

            self.ball.move(800, 600)
            
            
            pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()


if __name__== '__main__':
    pg.init()
    game= Game()
    game.main_loop()
    game.quit()

