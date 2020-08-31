import pygame
from batalladll import cercano, promedio

AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
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
pygame.font.init()  
# Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([1000, 800])
  
# Creamos un título para la ventana
pygame.display.set_caption('Juegazo de cuadraditos')
xnueva=0
ynueva=0
listade_todoslos_sprites = pygame.sprite.Group()
pos = pygame.mouse.get_pos() 

equipodiff = 0

# Creamos la serpiente inicial.
Arqueros= Soldado(ROJO, xnueva, ynueva, 220, 150, equipodiff)
IPesada = Soldado(ROJO, xnueva, ynueva, 1200, 30, equipodiff)
ILigera = Soldado(ROJO, xnueva, ynueva, 600, 60, equipodiff)
colisionador =pygame.Surface([170, 40])


#ArquerosAnima=pygame.image.load('Janso.jpg').convert()
#ArquerosAnima.set_colorkey(NEGRO)
reloj = pygame.time.Clock()
hecho = False

contadorsoldados = 0
soldado = []

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
    pantalla.fill(NEGRO)
    mouseinv=pygame.Surface([largodel_soldado, altodel_soldado])
    mouseinv.fill(BLANCO)
    pantalla.blit(mouseinv, (pos[0], pos[1]))
    colisionador.fill(BLANCO)
    pantalla.blit(colisionador, (0, 40))
    pygame.draw.line(pantalla, BLANCO, [200, 800 ], [200, 0], 2)
    fuente = pygame.font.Font(None, 25)
    texto = fuente.render("Mi texto", True, NEGRO)
    pantalla.blit(texto, [250, 250])
    
    if evento.type == pygame.MOUSEBUTTONDOWN:
        soldado.append(Soldado(ROJO, pos[0], pos[1], 600, 60, 1))
        
        listade_todoslos_sprites.add(soldado[contadorsoldados])
        contadorsoldados += 1

   
    pos = pygame.mouse.get_pos() 
    
    




    listade_todoslos_sprites.draw(pantalla)
              
    # Actualizamos la pantalla
    pygame.display.flip()
      
    # Pausa
    reloj.tick(60)
                  
pygame.quit()