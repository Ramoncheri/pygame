import pygame as pg
import sys

BGColor= (0,0,0)

class Game:

    def __init__(self):
        self.pantalla= pg.display.set_mode((800, 600))
        self.pantalla.fill(BGColor)
        pg.display.set_caption('Pong')

    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type== pg.QUIT:
                    game_over= True

            pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()


if __name__== '__main__':
    pg.init()
    game= Game()
    game.main_loop()
    game.quit()

