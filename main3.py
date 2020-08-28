import pygame
 

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
pantalla = pygame.display.set_mode([800, 600])
  
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
#ArquerosAnima=pygame.image.load('Janso.jpg').convert()
#ArquerosAnima.set_colorkey(NEGRO)
reloj = pygame.time.Clock()
hecho = False
  
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
    pantalla.fill(NEGRO)
    mouseinv=pygame.Surface([largodel_soldado, altodel_soldado])
    mouseinv.fill(BLANCO)
    pantalla.blit(mouseinv, (pos[0], pos[1]))
    
    if evento.type == pygame.MOUSEBUTTONDOWN and pos[0] <= 400:
        print("elegiste el equipo 1. ")
        print("tienes Arqueros, Infanteria pesada e infanteria ligera")
        print("tus x son desde 0 hasta 400")
        print("tus y son desde 0 hasta 600")
        tipo_soldado = input("que tipo de soldado quieres?")
        #equipodiff=1
        #ynueva=int(input("Dime las y"))
        #xnueva=int(input("Dime las x"))
        #if tipo_soldado.upper()== "ARQUEROS" or tipo_soldado == 1:
            #print("elegiste arqueros. ")
            #print("tropas muy debiles a golpes, pero disparan a distancia")
            #listade_todoslos_sprites.add(Arqueros)
        #if tipo_soldado.upper() == "INFANTERIA PESADA" or tipo_soldado==2:
            #print("elegiste la Infanteria pesada. ")
            #print("tropas muy fuertes a golpes, pero no hacen un daño considerable")
            #listade_todoslos_sprites.add(IPesada)
        #if tipo_soldado.upper() == "INFANTERIA LIGERA" or tipo_soldado==3:
            #print("elegiste la Infanteria ligera. ")
            #print("tropas estandar, con resistencia normal, su daño es estandar")
            #listade_todoslos_sprites.add(ILigera)
        # Establecemos la velocidad basándonos en la tecla presionada
        # Queremos que la velocidad sea la suficiente para mover un segmento
        # más el margen.
   
    pos = pygame.mouse.get_pos() 
 
    #offset = (xnueva, ynueva)  
    #pantalla.blit(ArquerosAnima, offset)    
    #listade_todoslos_sprites.add(Soldado(BLANCO, xnueva, ynueva, vidanueva, dañonueva, equiponueva))
       
    
    
    
            
    #equipo1.movimiento((equipo2.rect.x - (equipo1.rect.x) )/30, (equipo2.rect.y - (equipo1.rect.y))/30)

    #equipo2.movimiento((equipo1.rect.x - (equipo2.rect.x) )/30, (equipo1.rect.y - (equipo2.rect.y))/30)

    
    # -- Dibujamos todo
    # Limpiamos la pantalla
    
    
    #print(soldado1.vida)
    #print(soldado2.vida)
    listade_todoslos_sprites.draw(pantalla)
              
    # Actualizamos la pantalla
    pygame.display.flip()
      
    # Pausa
    reloj.tick(60)
                  
pygame.quit()