import pygame as pg
from pygame.locals import *
import sys, random
from sprites import *

BGColor= (0,0,0)
YELLOW= (255, 255, 0)
WHITE= (255, 255, 255)
win_score= 5

class Game:

    def __init__(self):
        pg.display.set_caption('Pong')
        self.pantalla= pg.display.set_mode((800, 600))
        self.pantalla.fill(BGColor)
        self.fondo= pg.image.load('./resources/image/fondo.jpg')
        self.fontMarcador= pg.font.Font('./resources/fonts/PressStart2P.ttf', 36)
        self.font= pg.font.Font('./resources/fonts/PressStart2P.ttf', 20)
        self.fontGrande= pg.font.Font('./resources/fonts/PressStart2P.ttf', 60)

        self.status= 'partida'

        self.marcadorOne= self.fontMarcador.render('0', True, WHITE)
        self.marcadorTwo= self.fontMarcador.render('0', True, WHITE)

        self.text_game_over = self.fontGrande.render('GAME OVER', True, YELLOW)
        self.text_insert_coin= self.font.render('<SPACE> - Inicio partida', True, WHITE)

        self.ball= Ball()

        self.playerOne= Raquet(30)
        self.playerTwo = Raquet(770)

        self.playersGroup=pg.sprite.Group()
        self.playersGroup.add(self.playerOne)
        self.playersGroup.add(self.playerTwo)

        self.allSprites = pg.sprite.Group()
        self.allSprites.add(self.ball)
        self.allSprites.add(self.playersGroup)

        self.scoreOne= 0
        self.scoreTwo= 0


    def handleEvent(self):
        
        for event in pg.event.get():   #EVENTOS
            if event.type== pg.QUIT:
                self.quit()
            
            if event.type == KEYDOWN:
                if event.key== K_w:
                    self.playerOne.vy = -5
                
                if event.key== K_z:
                    self.playerOne.vy = 5
                
            if event.type == KEYDOWN:
                if event.key== K_KP9:
                    self.playerTwo.vy = -5
                
                if event.key== K_KP3:
                    self.playerTwo.vy = 5
            
        key_pressed= pg.key.get_pressed()
        if key_pressed[K_w]:
            self.playerOne.vy = -5
        elif key_pressed[K_z]:
            self.playerOne.vy = 5
        else:
            self.playerOne.vy = 0

        if key_pressed[K_KP9]:
            self.playerTwo.vy = -5
        elif key_pressed[K_KP3]:
            self.playerTwo.vy = 5
        else:
            self.playerTwo.vy = 0
        
        return False

    def bucle_partida(self):
        game_over= False
        self.scoreOne = 0
        self.scoreTwo = 0
        self.marcadorOne= self.fontMarcador.render('0', True, WHITE)
        self.marcadorTwo= self.fontMarcador.render('0', True, WHITE)

        while not game_over:

            game_over= self.handleEvent()
            '''
            self.ball.update(800, 600)                #movimiento de los objetos
            self.playerOne.update(600)
            self.playerTwo.update(600)
            '''
            self.allSprites.update(800, 600)

            self.ball.comprobarChoque(self.playersGroup)
            '''
            self.ball.comprobarChoque(self.playerOne)
            self.ball.comprobarChoque(self.playerTwo)
            '''
            if self.ball.vx == 0 and self.ball.vy == 0:
                if self.ball.rect.centerx >= 800:
                    self.scoreOne += 1
                    self.marcadorOne= self.fontMarcador.render(str(self.scoreOne), True, WHITE)
     
                if self.ball.rect.centerx <= 0:
                    self.scoreTwo +=1
                    self.marcadorTwo= self.fontMarcador.render(str(self.scoreTwo), True, WHITE)
                if self.scoreOne == win_score or self.scoreTwo == win_score:
                    game_over= True

                
                self.ball.reset()

            self.pantalla.blit(self.fondo, (0, 0))  #que vas a pintar y su posicion
            '''
            self.pantalla.blit(self.ball.image, (self.ball.rect.x, self.ball.rect.y))               # pintado de los objetos en pantalla
            self.pantalla.blit(self.playerOne.image, (self.playerOne.rect.x, self.playerOne.rect.y))
            self.pantalla.blit(self.playerTwo.image, (self.playerTwo.rect.x, self.playerTwo.rect.y))
            '''
            self.allSprites.draw(self.pantalla)
            
            self.pantalla.blit(self.marcadorOne, (340, 10))
            self.pantalla.blit(self.marcadorTwo, (430, 10))

            pg.display.flip()

        self.status = 'Inicio'

    def bucle_inicio(self):
        inicio_partida = False
        while not inicio_partida:
            for event in pg.event.get():   #EVENTOS
                if event.type== QUIT:
                    self.quit()
                
                if event.type == KEYDOWN:
                    if event.key== K_SPACE:
                        inicio_partida= True

            self.pantalla.fill((0, 0, 255))
            self.pantalla.blit(self.text_game_over,(100, 100))
            self.pantalla.blit(self.text_insert_coin,(100, 200))

            pg.display.flip()

        self.status = 'partida'

    
    def main_loop(self):

        while True:

            if self.status== 'partida':
                self.bucle_partida()
            else:
                self.bucle_inicio()


    def quit(self):
        pg.quit()
        sys.exit()


if __name__== '__main__':
    pg.init()
    game= Game()
    game.main_loop()
    game.quit()

