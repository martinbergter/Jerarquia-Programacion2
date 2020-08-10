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
  
        # Establecemos como punto de partida la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
    def movimiento(self, x, y):

    	self.rect.y += y
    	self.rect.x += x
    
    def colision(self,x,y, vida, daño):
        if self.rect.x == self.rect.x + 40 and self.rect.y == self.rect.y + 40:
            self.vida -= self.daño
    
# Inicializamos Pygame
pygame.init()
  
# Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([800, 600])
  
# Creamos un título para la ventana
pygame.display.set_caption('Juegazo de cuadraditos')
 
listade_todoslos_sprites = pygame.sprite.Group()
pos = pygame.mouse.get_pos() 

# Creamos la serpiente inicial.
equipo1 = [Soldado(ROJO, pos[0], pos[1], 100, 50, 1), Soldado(ROJO, 790, 590, 200, 2, 2)]
equipo2 = [Soldado(BLANCO, 1, 1, 100, 50, 1), Soldado(BLANCO, 790, 590, 200, 2, 2)]


reloj = pygame.time.Clock()
hecho = False
listade_todoslos_sprites.add(equipo1, equipo2)  
while not hecho:
      
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
  
        # Establecemos la velocidad basándonos en la tecla presionada
        # Queremos que la velocidad sea la suficiente para mover un segmento
        # más el margen.
    
    pos = pygame.mouse.get_pos() 

    
    if evento.type == pygame.MOUSEBUTTONDOWN and pos[0] <= 400:
        tipo_soldado = equipo1[int(input("que tipo de soldado quieres?"))]
        listade_todoslos_sprites.add([tipo_soldado])
            
    #if evento.type == pygame.MOUSEBUTTONUP:
            #rayo = False
    
            
    #equipo1.movimiento((equipo2.rect.x - (equipo1.rect.x) )/30, (equipo2.rect.y - (equipo1.rect.y))/30)

    #equipo2.movimiento((equipo1.rect.x - (equipo2.rect.x) )/30, (equipo1.rect.y - (equipo2.rect.y))/30)

    
    # -- Dibujamos todo
    # Limpiamos la pantalla
    pantalla.fill(NEGRO)
    
    #print(soldado1.vida)
    #print(soldado2.vida)
    listade_todoslos_sprites.draw(pantalla)
              
    # Actualizamos la pantalla
    pygame.display.flip()
      
    # Pausa
    reloj.tick(10)
                  
pygame.quit()