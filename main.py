import pygame as pg
import sys

BGColor= (0,0,0)
YELLOW= (255, 255, 0)

class Ball:
    def __init__(self):
        self.vx= 5  #veloc. de x e y
        self.vy= 5
        self.x= 400
        self.y= 300
        self.w= 20  #ancho de la bola
        self.posX= self.x- self.w//2   # coordenada X para situar la bola en el centro de la pantalla
        self.h= 20   # alto de la bola
        self.posY= self.y- self.h//2

        self.image= pg.Surface((20, 20))
        self.image.fill(YELLOW)


class Game:

    def __init__(self):
        pg.display.set_caption('Pong')
        self.pantalla= pg.display.set_mode((800, 600))
        self.pantalla.fill(BGColor)
        fondo= pg.image.load('./resources/fondo.jpg')
        self.pantalla.blit(fondo, (0, 0))
        
        self.ball= Ball()

        

    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type== pg.QUIT:
                    game_over= True

            self.pantalla.blit(self.ball.image, (self.ball.posX, self.ball.posY))
            pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()


if __name__== '__main__':
    pg.init()
    game= Game()
    game.main_loop()
    game.quit()

