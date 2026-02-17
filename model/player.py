import pygame
import random
from pygame.locals import RLEACCEL
from settings import LARGURA,ALTURA
class Player(pygame.sprite.Sprite):
          def __init__(self,driver_name,team_name,image_pilot=None):
                    super (Player,self).__init__()
                    self.driver_name=driver_name
                    self.team_name=team_name
                    self.font=pygame.font.SysFont("arial",40)
                    self.surf=pygame.image.load(image_pilot).convert_alpha()
                    self.surf=pygame.transform.scale(self.surf,(150,150))
                    self.surf.set_colorkey((255,255,255),RLEACCEL)
                    self.rect=self.surf.get_rect()
                    self.rect.x=400
                    self.rect.y=600
                    self.spawn=(self.rect.x,self.rect.y)
          def update(self,pressed_keys):
                  self.speed=random.randint(4,10)
                  if pressed_keys[pygame.K_RIGHT]:
                        self.rect.x+=self.speed
                  if pressed_keys[pygame.K_LEFT]:
                          self.rect.x-=self.speed   
                                              
                  if self.rect.left<0:
                         self.rect.left=0
                  if self.rect.left>LARGURA:
                         self.rect.left=LARGURA
                  if self.rect.top<=0:
                         self.rect.top=0
                         self.rect.y+=self.speed
                  if self.rect.bottom>=ALTURA:
                         self.rect.bottom=ALTURA
                  if self.rect.right>=LARGURA:
                          self.rect.right=LARGURA
                         
          def draw(self,tela):
                  tela.blit(self.surf,self.rect)
                  texto=self.font.render(self.driver_name,True,(255,255,255))
                  texto_rect=texto.get_rect(center=(self.rect.x+100,self.rect.top-1))
                  tela.blit(texto,texto_rect)

                