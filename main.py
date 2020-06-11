import pygame as pg
from pygame.locals import *
import sys, random

BGColor= (0,0,0)
YELLOW= (255, 255, 0)
WHITE= (255, 255, 255)
win_score= 3

class Ball:
    def __init__(self):
        self.reset()
        self.w= 20  #ancho de la bola
        self.h= 20   # alto de la bola

        self.image= pg.Surface((self.w, self.h))
        self.image.fill(YELLOW)
        self.ping= pg.mixer.Sound('./resources/sounds/ping.wav')
        self.lost_point= pg.mixer.Sound('./resources/sounds/lost-point.wav')

        
    @property
    def posX(self):
        return  self.x- self.w//2   # coordenada X para situar la bola en el centro de la pantalla
        
    @property
    def posY(self):
        return self.y- self.h//2

    def move(self, limitSuperX, limitSuperY):
        if self.x >= limitSuperX or self.x <= 0:
            self.vx = 0
            self.vy = 0
            self.lost_point.play()
            
        if self.y >= limitSuperY or self.y <= 0:
            self.vy *= -1
            self.ping.play()

        self.x += self.vx
        self.y += self.vy


    def comprobarChoque(self, algo ): #el algo será el player1 y el player2
        dx= abs(self.x - algo.xr)
        dy= abs (self.y - algo.yr)

        if dx < (self.w + algo.wr)//2 and dy < (self.h + algo.hr)//2:
            self.vx *= -1
            self.x += self.vx
            self.y += self.vy
            self.ping.play()

    def reset(self):
        self.vx= 2 * random.choice([-2, -1, 1, 2]) #velocidad de la bola en  x e y
        self.vy= random.choice([-4, -2, 3, 4])
        self.x= 400
        self.y= 300

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

        self.scoreOne= 0
        self.scoreTwo= 0


    def handleEvent(self):
        
        for event in pg.event.get():   #EVENTOS
            if event.type== pg.QUIT:
                self.quit()
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
        
        return False

    def bucle_partida(self):
        game_over= False
        self.scoreOne = 0
        self.scoreTwo = 0
        self.marcadorOne= self.fontMarcador.render('0', True, WHITE)
        self.marcadorTwo= self.fontMarcador.render('0', True, WHITE)

        while not game_over:

            game_over= self.handleEvent()
            
            self.ball.move(800, 600)                #movimiento de los objetos
            self.playerOne.raquet_move(800, 600)
            self.playerTwo.raquet_move(800, 600)

            self.ball.comprobarChoque(self.playerOne)
            self.ball.comprobarChoque(self.playerTwo)
            
            if self.ball.vx == 0 and self.ball.vy == 0:
                if self.ball.x >= 800:
                    self.scoreOne += 1
                    self.marcadorOne= self.fontMarcador.render(str(self.scoreOne), True, WHITE)
     
                if self.ball.x <= 0:
                    self.scoreTwo +=1
                    self.marcadorTwo= self.fontMarcador.render(str(self.scoreTwo), True, WHITE)
                if self.scoreOne == win_score or self.scoreTwo == win_score:
                    game_over= True

                
                self.ball.reset()

            self.pantalla.blit(self.fondo, (0, 0))  #que vas a pintar y su posicion
            self.pantalla.blit(self.ball.image, (self.ball.posX, self.ball.posY))               # pintado de los objetos en pantalla
            self.pantalla.blit(self.playerOne.image, (self.playerOne.posX, self.playerOne.posY))
            self.pantalla.blit(self.playerTwo.image, (self.playerTwo.posX, self.playerTwo.posY))
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

