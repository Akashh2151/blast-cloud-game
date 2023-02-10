def new_word():                                    #def funtion use kel aahe 
    global word_x,word_y,text,choseen_word,press_word,speed                      
    word_x=random.randint(100,600)                 #word x variable ghetl ani tya madhe yeanr je word aahe te 100 te 600 cha madhe show honya sathi 100 ani 600 takl
    word_y=0
    press_word=''
    speed += 0                                  # zero thevl karan zero paun word khalial pahijel na. akash dada
    choseen_word=random.choice(list)               #list  madil random word chose karnya sathi aahe
    text = font.render(choseen_word,True,red)       # font la render karun show kart 
from os import P_OVERLAY
import pygame
import sys
import random
pygame.init() # inisilize kart pygame la...

################################## color
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
##################################variable
x=800
y=600
speed=0.2
point=0
list=['akash','priti','hello','chinu','papya']
font=pygame.font.SysFont('ComicSansMs',45)
text1 =font.render('hit enter to restart the game',True,red)  # y600 ghetl aahe te word khali yenar k tharavik thikani ale ki lose hoil mhanje game restart hoil ani te show karel
############################# screen
win= pygame.display.set_mode((x,y))                   # display banavnya sathi he use kel jat
pygame.display.set_caption('CODE WITH EDISON')         # game ch name set krt 
##############################imgagews
lobo=pygame.image.load('bird.png')                     #lobo name cha variabel ghetl ani img load keli icon chi
pygame.display.set_icon(lobo)                          #lod keli img var ania aata ti icon la setkeli 
background1=pygame.image.load('background 1.jpg') 
letter_back_img=pygame.image.load('demon1.png') 
################################### call kela def funtion la
new_word()
################################################## sound
pygame.mixer.music.load('aline.mp3')      #set volume in background
# pygame.mixer.music.set_volume()    value chi speed karyc ky garaj nhiii 
pygame.mixer.music.play()
chanel10=pygame.mixer.Channel(0)     #te var lod kel music and ithe play karun takl akash
chanel11=pygame.mixer.Channel(1)     #te var lod kel music and ithe play karun takl akash
lostmusic=pygame.mixer.Sound('die.wav')
############################# infinite game loop
while True:
    win.blit(background1,(0,0))                               # blit name cha ik funtion aahe te refresh kart  pratek veli wn madhe gheun x and y cha size n dili tyala
    win.blit(letter_back_img,(word_x-9,word_y-55))            #back side img set keli aahe 
    win.blit(text,(word_x,word_y))                            #backside cha img cha varil text akash dada                            #backside cha img cha varil text akash dada 
    word_y += speed
    word_capstion=font.render(choseen_word,True,red)   #left side la je same word yety tya sathiaahe
    win.blit(word_capstion,(10,50))                    #alwalys show kart te word left side cha
    # pass                                             #pass stetment lavl ki code hang kart display hang kart 
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        
        elif(event.type==pygame.KEYDOWN):
            press_word += pygame.key.name(event.key)
            if choseen_word.startswith(press_word):
               text=font.render(press_word,True,blue)
    
               if(choseen_word == press_word):
                  point += len(choseen_word)
                  chanel10.play(pygame.mixer.Sound('swoosh.wav'),maxtime=1000) #var sound madhe chanel banvli aahet tyatil ik canel use karun music set kel aahe 
                  chanel10.set_volume(1)   # volume set kel aahe
                  new_word()
            else:
                text=font.render(press_word,True,red)   
                press_word=''

    point_capstion=font.render(str(point),True,blue)   #score sathi aahe help                                      #sys error nhi ky det niwant madhe quit hot var import kel aahe sys
    win.blit(point_capstion,(10,5))                    #score  
    
    if(word_y < y-5):
        pass
    else:
        bb=pygame.mixer.Channel(1).get_busy()           #chanel1muic play both of time so if abd else condition are use and get busy fution use to stop music
        if bb == 1:
            pass
        else:
          chanel11.play(lostmusic,maxtime=100000)   #set volume of lostmucic
        win.blit(text1,(100,260)) 
        pygame.display.update()
        event=pygame.event.wait()
        if(event.type==pygame.QUIT):
            pygame.QUIT()
            sys.exit()
        if(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
           point=0
           speed=0.1
           new_word()    
    
    pygame.display.update()