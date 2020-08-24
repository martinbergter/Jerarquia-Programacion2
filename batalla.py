import pygame
 

AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
 

largodel_soldado = 15
altodel_soldado = 15

margendel_soldado = 3
 
def cercano(num,collection):
   return min(collection,key=lambda x:abs(x-num))

class Soldado(pygame.sprite.Sprite):
    """ Clase que representa un segmento del soldado """

    def __init__(self, color, x, y, vida, daño, equipo ):
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

    def ataque(lista):
        a = cercano(self.y, lista)
        return (self.y+a)/2

def batalla(lista_soldados):
  print("BATALLA")
  for i in lista_soldados:
      lista_soldados[i].movimiento(400, lista_soldados[i].ataque(lista_soldados))
    
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

fuente = pygame.font.Font(None, 25)
texto1 = fuente.render("Arqueros", True, BLANCO)
pantalla.blit(texto1, [250, 250])
# Creamos la serpiente inicial.
Arqueros = Soldado(ROJO, 200, 150, 100, 50, 1)
equipo2 = [Soldado(BLANCO, 1, 1, 100, 50, 2), Soldado(BLANCO, 790, 590, 200, 2, 2)]
soldado1 = Soldado(ROJO, 1, 1, 100, 50, 1)
soldado2 = Soldado(BLANCO, 20, 20, 200, 2, 2)

reloj = pygame.time.Clock()
hecho = False
  
listade_todoslos_sprites.add(soldado1, soldado2) 
lista_personajes = {soldado1, soldado2}

while not hecho:
      
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
  
        # Establecemos la velocidad basándonos en la tecla presionada
        # Queremos que la velocidad sea la suficiente para mover un segmento
        # más el margen.
    
    pos = pygame.mouse.get_pos() 
    listade_todoslos_sprites.add(soldado1, soldado2)
    listade_todoslos_sprites.draw(pantalla)
    if int(input("escribi 1 pàra empezar la batalla")) == 1:
        batalla(lista_personajes)



        
        #listade_todoslos_sprites.add(Soldado(BLANCO, xnueva, ynueva, vidanueva, dañonueva, equiponueva))
            
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
    reloj.tick(60)
                  
pygame.quit()