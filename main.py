import pygame
import sys
import json
import os
import requests
from pygame.locals import MOUSEBUTTONDOWN,KEYDOWN,K_RETURN,K_p,K_ESCAPE,QUIT
from settings import LARGURA,ALTURA
from model.player import Player
from model.car import car,CARRO_POS
from game_stats import MENU,LOJA,JOGANDO,CONFIGURACOES,CREDITOS,PILOTOS,EQUIPES,VITORIA,INICIO,DERROTA,CARREGANDO
pygame.init()
pygame.mixer.init()
fonte=pygame.font.SysFont("arial",36)
fonte_botao=pygame.font.SysFont("arial",15)
tela=pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("pole position")
capa=pygame.image.load("imagens/Capacete.png")
pygame.display.set_icon(capa)
bg=pygame.image.load("imagens/Menu inicial.png").convert()
bg=pygame.transform.scale(bg,(LARGURA,ALTURA))
shop=pygame.image.load("imagens/Loja.png").convert()
shop=pygame.transform.scale(shop,(LARGURA,ALTURA))
selecao_p=pygame.image.load("imagens/Escolha de pilotos.png").convert()
selecao_p=pygame.transform.scale(selecao_p,(LARGURA,ALTURA))
selecao_e=pygame.image.load("imagens/Escolha de equipes.png").convert()
selecao_e=pygame.transform.scale(selecao_e,(LARGURA,ALTURA))
win=pygame.image.load("imagens/interlagos.png").convert()
win=pygame.transform.scale(win,(LARGURA,ALTURA))
fundo_game=pygame.image.load("imagens/pista.png").convert()
fundo_game=pygame.transform.scale(fundo_game,(LARGURA,ALTURA))
c=pygame.image.load("imagens/Configuracoes.png")
c=pygame.transform.scale(c,(LARGURA,ALTURA))
creditos=pygame.image.load("imagens/Creditos.png")
creditos=pygame.transform.scale(creditos,(LARGURA,ALTURA))
clock=pygame.time.Clock()
team_name="nenhuma"
driver_name="vazio"
image_pilot="imagens/Capacete.png"
player_criado=0
teams={"legend":False,
       "redbull":True,
       "mclaren":True,
       "mercedes":True,
       "ferrari":True
}
pilots={"king":False,
        "hamilton":True,
        "senna":True,
        "schumacher":True,
        "verstappen":True
}
historico=[]
BRANCO=(255,255,255)
estado_anterior=MENU
tocando=True
som_botao=pygame.mixer.Sound("som/Slap with Glove.mp3")
def desenhar_botao(cor,x,y,largura,altura):
     pygame.draw.rect(tela,cor,(x,y,largura,altura),border_radius=10)
     return pygame.Rect(x,y,largura,altura)
def botao_com_texto(cor,x,y,largura,altura,texto,cor_texto,fonte):
     pygame.draw.rect(tela,cor,(x,y,largura,altura),border_radius=10)
     texto_render=fonte.render(texto,True,cor_texto)
     tela.blit(texto_render,(x+10,y+10))
     return pygame.Rect(x,y,largura,altura)
def desenhar_barra(progresso):
     largura=400
     altura=40
     x=200
     y=500
     pygame.draw.rect(tela,(100,100,100),(x,y,largura,altura),border_radius=10)
     pygame.draw.rect(tela,(255,0,0),(x,y,largura*progresso,altura),border_radius=10)
if tocando==True:
    pygame.mixer.music.load("som/GTA type Beat - Dyalla.mp3")
    pygame.mixer.music.play(-1)
def menu_inicial():
   global botao1,botao2,botao3,botao4,tempo,historico,driver_name,team_name,partida,pts
   if os.path.exists("dados/historico.json"):
        with open("dados/historico.json","r") as arq:
                 historico= json.load(arq)
   else:
        historico=[]
 
   while True:  
          botao1=desenhar_botao(BRANCO,50,480,200,50)         
          botao2=desenhar_botao(BRANCO,50,350,200,50)     
          botao3=desenhar_botao(BRANCO,50,420,200,50)         
          botao4=desenhar_botao(BRANCO,50,535,200,50)
          tela.blit(bg,(0,0)) 
          for event in pygame.event.get():
                  if event.type==MOUSEBUTTONDOWN:
                    if botao1.collidepoint(event.pos):
                        som_botao.play()
                        return LOJA
                    elif botao2.collidepoint(event.pos):
                         som_botao.play()
                         tempo=pygame.time.get_ticks()
                         return CARREGANDO
                    elif botao3.collidepoint(event.pos):
                         som_botao.play()
                         return CONFIGURACOES
                    elif botao4.collidepoint(event.pos):
                         som_botao.play()
                         return CREDITOS
                  elif event.type==QUIT:
                          pygame.quit()
                          sys.exit()
          pygame.display.flip() 
          clock.tick(15)
def carregar():
     global tempo_inicio,duracao,progresso,BRANCO,tempo,mensagem,texto,tocando
     while True:
          tempo_inicio=pygame.time.get_ticks()-tempo
          duracao= 2000
          progresso=min(tempo_inicio/duracao,1)
          carga=100*progresso
          carga=int(carga)
          for event in pygame.event.get():
               if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
          tela.fill((0,0,0))
          desenhar_barra(progresso)
          mensagem=f"carregando... {carga} %"
          texto=fonte.render(mensagem,True,(BRANCO))
          tela.blit(texto,(300,400))
          if progresso>=1 and estado_anterior==MENU:
               return PILOTOS
          if progresso>=1 and estado_anterior==PILOTOS:
               return MENU
          if progresso>=1 and estado_anterior==EQUIPES:
               return INICIO
          if progresso>=1 and estado_anterior==DERROTA :
               if tocando==True:
                 pygame.mixer.music.play(-1)
               return MENU 
          if progresso>=1 and estado_anterior==VITORIA:
                if tocando==True:
                   pygame.mixer.music.play(-1)
                return MENU  
          pygame.display.flip()
          clock.tick(30)
def loja():
        global teams,mensagem,texto,botao1
        mensagem=""
        while True:
            botao1=desenhar_botao(BRANCO,100,105,100,40)
            tela.blit(shop,(0,0))
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                     if event.key==K_p:
                          pilots["king"]=True
                          teams["legend"]=True
                          mensagem="team Legend unlock"
                elif event.type==MOUSEBUTTONDOWN:
                     if botao1.collidepoint(event.pos):
                          som_botao.play()
                          return MENU 
                if event.type==QUIT:
                      pygame.quit()
                      sys.exit() 
            texto= fonte.render(mensagem,True,(0,0,0))       
            tela.blit(texto,(300,100))
            pygame.display.flip()
            clock.tick(15)
def configuracoes():
     global botao1,botao2,botao3,texto1,texto2,texto3,tocando
     texto1="sair"
     texto2="desativar musica"
     texto3="ativar musica"
     while True:       
          botao2=botao_com_texto(BRANCO,420,395,325,100,texto2,(255,0,0),fonte_botao)
          botao3=botao_com_texto(BRANCO,50,395,325,100,texto3,(255,0,0),fonte_botao)
          tela.blit(c,(0,0))
          for event in pygame.event.get():
               if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                         som_botao.play()
                         return MENU
               if event.type==MOUSEBUTTONDOWN:
                    if botao2.collidepoint(event.pos):
                         som_botao.play()
                         tocando=False
                         pygame.mixer.music.stop()
                    if botao3.collidepoint(event.pos):
                              som_botao.play()
                              tocando=True
                              pygame.mixer.music.play(-1)
               if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
          pygame.display.flip()
          clock.tick(15)
def creditos_game():
     global botao1,mensagem,botao2,botao3,texto,PRETO
     PRETO=((0,0,0))
     mensagem=""
     while True:
          tela.blit(creditos,(0,0))
          for event in pygame.event.get():
               if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                         som_botao.play()
                         return MENU
               if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
          texto=fonte.render(mensagem,True,(255,0,0))
          tela.blit(texto,(100,100))
          pygame.display.flip()
          clock.tick(15)
def selecao_pilotos():
     global driver_name,botao1,botao2,botao3,botao4,botao5,botao6,tempo
     while True:
          botao1=desenhar_botao(BRANCO,250,123,90,80)
          botao2=desenhar_botao(BRANCO,250,210,90,70)
          botao3=desenhar_botao(BRANCO,250,285,90,75)
          botao4=desenhar_botao(BRANCO,250,365,90,75)
          botao5=desenhar_botao(BRANCO,250,446,90,78)
          botao6=desenhar_botao(BRANCO,200,10,100,30)
          tela.blit(selecao_p,(0,0))
          for event in pygame.event.get():
               if event.type==MOUSEBUTTONDOWN:
                    if botao1.collidepoint(event.pos) and player_criado==0 and pilots["senna"]==True:
                         som_botao.play()
                         driver_name="senna"
                         return EQUIPES
                    if botao2.collidepoint(event.pos) and player_criado==0 and pilots["verstappen"]==True:
                         som_botao.play()
                         driver_name="verstappen"
                         return EQUIPES
                    if botao3.collidepoint(event.pos) and player_criado==0 and pilots["hamilton"]==True:
                         som_botao.play()
                         driver_name="hamilton"
                         return EQUIPES
                    if botao4.collidepoint(event.pos) and player_criado==0 and pilots["schumacher"]==True:
                         som_botao.play()
                         driver_name="schumacher"
                         return EQUIPES
                    if botao5.collidepoint(event.pos) and player_criado==0 and pilots["king"]==True:
                         som_botao.play()
                         driver_name="king"
                         return EQUIPES
                    if botao6.collidepoint(event.pos):
                         som_botao.play()
                         tempo=pygame.time.get_ticks()
                         return CARREGANDO
               if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
          pygame.display.flip()
          clock.tick(15)
def selecao_equipes():
     global team_name,image_pilot,player_criado,teams,driver_name,botao1,botao2,botao3,botao4,tempo
     while True:
          botao1=desenhar_botao(BRANCO,150,108,100,118)
          botao2=desenhar_botao(BRANCO,150,230,100,100)
          botao3=desenhar_botao(BRANCO,150,333,100,94)
          botao4=desenhar_botao(BRANCO,150,433,107,75)
          botao5=desenhar_botao(BRANCO,150,513,100,70)
          tela.blit(selecao_e,(0,0))
          for event in pygame.event.get():
               if event.type==KEYDOWN:
                    som_botao.play()
                    if event.key==K_ESCAPE:
                         return PILOTOS
               if event.type==MOUSEBUTTONDOWN:
                    if  botao1.collidepoint(event.pos) and player_criado==0 and teams["ferrari"]==True:
                         som_botao.play()
                         team_name="ferrari"
                         if driver_name=="senna":
                              image_pilot="imagens/Senna-Ferrari.png"
                              player_criado+=1
                         if driver_name=="hamilton":
                              image_pilot="imagens/Hamilton-Ferrari.png"
                              player_criado+=1
                         if driver_name=="schumacher":
                              image_pilot="imagens/Schumacher-Ferrari.png"
                              player_criado+=1
                         if driver_name=="king":
                              image_pilot="imagens/Schumacher-Ferrari.png"
                              player_criado+=1
                         if driver_name=="verstappen":
                              image_pilot="imagens/Verstappen-Ferrari.png"
                              player_criado+=1
                    elif botao2.collidepoint(event.pos) and player_criado==0 and teams["mclaren"]==True:
                        som_botao.play()
                        team_name="mclaren"
                        if driver_name=="senna":
                             image_pilot="imagens/Senna-Mclaren.png"
                             player_criado+=1
                        if driver_name=="hamilton":
                              image_pilot="imagens/Hamilton-Mclaren.png"
                              player_criado+=1
                        if driver_name=="king":
                              image_pilot="imagens/Senna-Mclaren.png"
                              player_criado+=1
                        if driver_name=="schumacher":
                              image_pilot="imagens/Schumacher-Mclaren.png"
                              player_criado+=1
                        if driver_name=="verstappen":
                              image_pilot="imagens/Verstappen-Mclaren.png"
                              player_criado+=1
                    elif botao3.collidepoint(event.pos) and player_criado==0 and teams["mercedes"]==True:
                         som_botao.play()
                         team_name="mercedes"
                         if driver_name=="senna":
                              image_pilot="imagens/Senna-Mercedes.png"
                              player_criado+=1
                         if driver_name=="hamilton":
                              image_pilot="imagens/Hamilton-Mercedes.png"
                              player_criado+=1
                         if driver_name=="king":
                              image_pilot="imagens/Hamilton-Mercedes.png"
                              player_criado+=1
                         if driver_name=="schumacher":
                              image_pilot="imagens/Schumacher-Mercedes.png"
                              player_criado+=1
                         if driver_name=="verstappen":
                              image_pilot="imagens/Verstappen-Mercedes.png"
                              player_criado+=1
                    elif botao4.collidepoint(event.pos) and player_criado==0 and teams["redbull"]==True:
                         som_botao.play()
                         if driver_name=="senna":
                              image_pilot="imagens/Senna-Redbull.png"
                              player_criado+=1
                         if driver_name=="hamilton":
                              image_pilot="imagens/Hamilton-Redbull.png"
                              player_criado+=1
                         if driver_name=="schumacher":
                              image_pilot="imagens/Schumacher-Redbull.png"
                              player_criado+=1
                         if driver_name=="verstappen":
                              image_pilot="imagens/Verstappen-Redbull.png"
                              player_criado+=1
                         if driver_name=="king":
                              image_pilot="imagens/Verstappen-Redbull.png"
                              player_criado+=1
                    elif botao5.collidepoint(event.pos)  and player_criado==0 and teams["legend"]==True:
                         som_botao.play()
                         team_name="legend"        
                         image_pilot="imagens/KING.png"
                         player_criado+=1            
                    if player_criado>0:
                         tempo=pygame.time.get_ticks()
                         return CARREGANDO
               if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
          pygame.display.flip()
          clock.tick(15)
partida=0
def inicio_jogo():
     global partida,team_name,image_pilot,player_criado,driver_name,texto,time,time_set,time_now,mensagem,BRANCO
     pygame.mixer.music.stop()
     time=pygame.time.get_ticks()
     while True:
          tela.fill((BRANCO))
          for event in pygame.event.get():
             if event.type==QUIT:
               pygame.quit()
               sys.exit()
          time_set=pygame.time.get_ticks()  
          time_now=(time_set-time)//1000
          if time_now<=3:
               mensagem=f"{time_now}"
          if time_now>3: 
               mensagem=""
               partida+=1

               return JOGANDO
          texto=fonte.render(mensagem,True,(0,0,0))
          tela.blit(texto,(400,300))
          pygame.display.flip()
          clock.tick(15)
def jogar():
     global historico,jogo,partida,barreira,barreira2,ret_player,pts,y,fundo_y,vel_y,player,carro,all_sprites,player_criado,driver_name,team_name,npc,timer,timer_set,timer_now,fonte,texto
     timer=pygame.time.get_ticks()
     fundo_y=0    
     vel_y=20
     pts=0
     ultrapassagem=False
     player=Player(driver_name,team_name,image_pilot)
     carro=car()
     all_sprites=pygame.sprite.Group()
     all_sprites.add(player)
     npc=pygame.sprite.Group()
     npc.add(carro)
     while True:              
          ret_player=desenhar_botao(BRANCO,0,300,800,1)
          barreira=desenhar_botao(BRANCO,0,0,55,600)
          barreira2=desenhar_botao(BRANCO,740,0,70,600)
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
          pressed_keys=pygame.key.get_pressed()
          timer_set=pygame.time.get_ticks()
          timer_now=(timer_set-timer)//1000
          if carro.rect.colliderect(ret_player):
             if not ultrapassagem:
               pts+=1
             else:
                  ultrapassagem=False 
          fundo_y+=vel_y

          if fundo_y >= ALTURA:
              fundo_y = 0
          tela.blit(fundo_game,(0,fundo_y))
          tela.blit(fundo_game,(0,fundo_y-ALTURA))
          player.update(pressed_keys)
          npc.update()
          texto=fonte.render(f"voce fez {pts} pontos",True,(255,255,255))
          tela.blit(texto,(30,30))
          for entity in all_sprites:
               tela.blit(entity.surf,entity.rect)
          player.draw(tela)
          carro.draw(tela)
          if pygame.sprite.spritecollideany(player,npc):
               player.kill()
               player_criado=0               
               jogo={"partida":partida,"piloto":driver_name,"equipe":team_name,"pontos":pts,"resultado":"derrota"}
               historico.append(jogo)
               with open ("dados/historico.json","w") as arq:
                    json.dump(historico,arq,indent=4)
               
               return DERROTA
          if barreira.colliderect(player) or barreira2.colliderect(player):
               player.kill()
               player_criado=0
               jogo={"partida":partida,"piloto":driver_name,"equipe":team_name,"pontos":pts,"resultado":"derrota"}
               historico.append(jogo)
               with open ("dados/historico.json","w") as arq:
                    json.dump(historico,arq,indent=4)
               
               return DERROTA
          if pts>=145 and timer_now==10:
               player_criado=0
               jogo={"partida":partida,"piloto":driver_name,"equipe":team_name,"pontos":pts,"resultado":"vitoria"}
               historico.append(jogo)
               with open ("dados/historico.json","w") as arq:
                    json.dump(historico,arq,indent=4)
               
               return VITORIA
          elif pts<152 and timer_now==10:
               player_criado=0
               jogo={"partida":partida,"piloto":driver_name,"equipe":team_name,"pontos":pts,"resultado":"derrota"}
               historico.append(jogo)
               with open ("dados/historico.json","w") as arq:
                    json.dump(historico,arq,indent=4)
              
               return DERROTA
          pygame.display.flip()
          clock.tick(60)
def vencedores():
     global tempo
     while True:
          for event in pygame.event.get():
               if event.type==KEYDOWN:
                    if event.key==K_RETURN:
                         tempo=pygame.time.get_ticks()
                         return CARREGANDO
               if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
          tela.blit(win,(0,0))  
          pygame.display.flip() 
          clock.tick(15)   
def perdeu():
     global BRANCO,mensagem,texto,tempo
     while True:    
          for event in pygame.event.get():
                if event.type==QUIT: 
                     pygame.quit()
                     sys.exit()
                if event.type==KEYDOWN:
                     if event.key==K_RETURN:
                          tempo=pygame.time.get_ticks()
                          return CARREGANDO
          tela.fill((BRANCO)) 
          mensagem="you lose :( , press enter" 
          texto=fonte.render(mensagem,True,(0,0,0))  
          tela.blit(texto,(200,300))   
          pygame.display.flip() 
          clock.tick(15)
estado=MENU
while True: 
       if estado==MENU:
             estado_anterior=MENU
             estado=menu_inicial()  
       if estado==LOJA:
           estado=loja()  
       if estado==CONFIGURACOES:
            estado=configuracoes()
       if estado==CREDITOS:
            estado=creditos_game()
       if estado==CARREGANDO:
            estado=carregar()
       if estado==PILOTOS:
            estado_anterior=PILOTOS
            estado=selecao_pilotos()
       if estado==EQUIPES:
            estado_anterior=EQUIPES
            estado=selecao_equipes()
       if estado==INICIO:
            estado=inicio_jogo()
       if estado==JOGANDO :                                        
             estado=jogar() 
       if estado==VITORIA:
            estado_anterior=VITORIA
            estado=vencedores()  
       if estado==DERROTA:
            estado_anterior=DERROTA
            estado=perdeu()      
