import pygame
 

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
 

largodel_soldado = 15
altodel_soldado = 15

margendel_soldado = 3
 


 
class Soldado(pygame.sprite.Sprite):
    """ Clase que representa un segmento del soldado """

    def __init__(self, color, x, y, vida, daño, equipo):
        # Llamada al constructor padre
        super().__init__()
        
        self.equipo = equipo  
        # Establecemos el alto y largo
        self.color = color
        self.image = pygame.Surface([largodel_soldado, altodel_soldado])
        self.image.fill(self.color)
        
        self.vida = vida
        self.daño = daño

        self.y = y
        self.x = x

        # Establecemos como punto de partida la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def movimiento(self, x, y):

        self.rect.y += y
        self.rect.x += x
    	
# Inicializamos Pygame
pygame.init()
  
# Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([800, 600])
  
# Creamos un título para la ventana
pygame.display.set_caption('Juegazo de cuadraditos')
 
listade_todoslos_sprites = pygame.sprite.Group()
 
# Creamos la serpiente inicial.


reloj = pygame.time.Clock()
hecho = False
  
soldado1 = Soldado(ROJO, 0, 0, 100, 50, 1)
soldado2 = Soldado(BLANCO, 30, 0, 200, 2, 2)

listade_todoslos_sprites.add(soldado1, soldado2)

while not hecho:
      
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
  
        # Establecemos la velocidad basándonos en la tecla presionada
        # Queremos que la velocidad sea la suficiente para mover un segmento
        # más el margen.


    soldado1.movimiento(0, 2)
    soldado2.movimiento(1, 3)
    
    # -- Dibujamos todo
    # Limpiamos la pantalla
    pantalla.fill(NEGRO)
    

    

    listade_todoslos_sprites.draw(pantalla)

    
              
    # Actualizamos la pantalla
    pygame.display.flip()
      
    # Pausa
    reloj.tick(60)
                  
pygame.quit()