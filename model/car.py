import pygame
import random 
from pygame.locals import RLEACCEL
from settings import LARGURA,ALTURA

class car(pygame.sprite.Sprite):
          def __init__(self):
                  super(car,self).__init__()
                  self.surf=pygame.image.load("imagens/Senna.png").convert_alpha()
                  self.surf=pygame.transform.scale(self.surf,(150,150))
                  self.surf.set_colorkey((255,255,255),RLEACCEL)
                  self.x=330
                  self.y=0              
                  self.spawn=(self.x,self.y)
                  self.rect=self.surf.get_rect(
                          center=(
                                  self.x,
                                  self.y,                             
                          )
                  )
          def update(self):
                  lista=[-1,0,0,0,1]
                  self.speed=random.randint(3,7)
                  self.new_speed=random.randint(3,7)
                  while self.speed==self.new_speed:
                          self.new_speed=random.randint(3,7)
                  self.speed=self.new_speed   
                  self.curva= random.choice(lista) 
                  self.rect.move_ip(self.curva,+self.speed)
                  if self.rect.left<0:
                         self.rect.left=0
                  if self.rect.left>LARGURA:
                         self.rect.left=LARGURA
                  if self.rect.top<=0:
                         self.rect.top=0       
                  if self.rect.bottom>750:
                         self.rect.top=0
          def draw(self,tela):
                if self.rect.topright>self.spawn:
                  tela.blit(self.surf,self.rect)