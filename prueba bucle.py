import pygame
import sys

pygame.init()

clock = pygame.time.Clock()


pantalla= pygame.display.set_mode((600, 400))

pygame.display.set_caption('Hola mundo')  #titulo de la pantalla

rojo= 0
direcc= 1

juego_activo= True

while juego_activo:
    #clock.tick(100)
    for event in pygame.event.get():   #Eventos
        if event.type== pygame.QUIT:
            juego_activo= False
            
    
    if rojo >= 255:
        direcc = -1

    if rojo <= 0:

        direcc = 1      #cambios
        
    rojo += direcc
    
    pantalla.fill((rojo, 0, 0))

    pygame.display.flip()   #pintar pantalla
    pygame.time.delay(5)
                
pygame.quit()
sys.exit()
    


