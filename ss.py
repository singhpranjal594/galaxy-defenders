import pygame
import random
import math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
#icon and window
pygame.display.set_caption("galaxy defenders")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
background=pygame.image.load('download.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
#player
playerimg=pygame.image.load("player.png")
playerx=370
playery=480
playerxchange=0
#enemy
enemyimg=[]
enemyx=[]
enemyy=[]
enemyxchange=[]
enemyychange=[]
numofenemies=10
for i in range(numofenemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,800))
    enemyy.append(random.randint(50,150))
    enemyxchange.append(4)
    enemyychange.append(40)
#bullet
bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=480
bulletxchange=0
bulletychange=10
bulletstate="ready"
distance=0
#score
scorevalue=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
overfont=pygame.font.Font('freesansbold.ttf',64)
def showscore(x,y):
    score=font.render("Score:"+str(scorevalue),True,(0,255,0))
    screen.blit(score,(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x+16,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
    if distance < 27:
        return True
    return False
def gameovertext(x,y):
    overtext=overfont.render("GAME OVER!!!",True,(255,0,0))
    screen.blit(overtext,(x,y))
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #if check key is left or right if pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange=-5
            if event.key == pygame.K_RIGHT:
                playerxchange=5
            if event.key == pygame.K_SPACE:
                if bulletstate is "ready":
                    bulletsound=mixer.Sound('laser.wav')
                    bulletsound.play()
                    bulletx=playerx
                    firebullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxchange=0
    #boundaries for player       
    playerx += playerxchange
    if playerx <=0:
        playerx=0
    elif playerx >=736:
        playerx=736
    player(playerx,playery)
    #movement of enemy
    for i in range(numofenemies):
        #gameover
        if enemyy[i]>440:
            for j in range(numofenemies):
                enemyy[j]=2000
            gameovertext(255,255)
            break
        enemyx[i]+=enemyxchange[i]
        if enemyx[i] <=0:
            enemyxchange[i]=4
            enemyy[i] += enemyychange[i]
        elif enemyx [i]>=736:
            enemyxchange[i]=-4
            enemyy[i] += enemyychange[i]
        collison=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collison:
            explosionsound=mixer.Sound('explosion.wav')
            explosionsound.play()
            bullety=480
            bulletstate="ready"
            scorevalue+=1
            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)
    #bullet movement
    if bullety <=0:
        bullety=480
        bulletstate="ready"
    if bulletstate is "fire":
        firebullet(bulletx,bullety)
        bullety -=bulletychange
    showscore(textx,texty)
    pygame.display.update()
    #nice game

            



