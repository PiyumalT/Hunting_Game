import pygame
import time
import random
import math

screen_high=357
screen_width=626

pygame.init()
screen=pygame.display.set_mode((screen_width, screen_high),pygame.RESIZABLE)
#pygame.display.set_caption("  Space inverders ")
#icon=pygame.image.load("icon.png")
background=pygame.image.load("data\\bg.jpg")
background2=pygame.image.load("data\\bg-2.png")
#pygame.display.set_icon(icon)

#player
speed=1
score=0
bullets_left=6
t56_mod=False


#pointer
pointer_img=pygame.image.load("data\\pointer.png")
bullet_sound=pygame.mixer.Sound("data\\gun.wav")
music=pygame.mixer.music.load("data\\Birds.mp3")
pygame.mixer.music.play(-1)
t56_sound=pygame.mixer.Sound("data\\t56.wav")
gun_load_sound=pygame.mixer.Sound("data\\gun_load.wav")
m_gun_img=pygame.image.load("data\\m_gun.png")
handgun_img=pygame.image.load("data\\handgun.png")
gun_type="handgun"
fire_ready=True
gun_loading_time=0

#Animals
animal_x=[]
animal_y=[]
animal_img_num=[]
animal_running=[]
num_of_animals=5
dead_animal_x=[]
dead_animal_y=[]
dead_animal_t=[]
animal_img=[pygame.image.load("data\\deer-1.png"),pygame.image.load("data\\deer-2.png")]
animal_run_img=[pygame.image.load("data\\deer-run-1.png"),pygame.image.load("data\\deer-run-2.png"),pygame.image.load("data\\deer-run-2.png"),pygame.image.load("data\\deer-run-1.png")]
dead_animal_img=[pygame.image.load("data\\dead-1.png"),pygame.image.load("data\\dead-2.png"),pygame.image.load("data\\dead-3.png")]

for i in range(num_of_animals):
  animal_x.append(100*i+random.randint(50,400))
  animal_y.append(random.randint(150,260))
  animal_img_num.append(random.randint(0,1))
  animal_running.append(0)

#fonts
font=pygame.font.Font('freesansbold.ttf',32)
ofont=pygame.font.Font('freesansbold.ttf',15)
rfont=pygame.font.Font('freesansbold.ttf',20)
over_font=pygame.font.Font('freesansbold.ttf',64)
textx,texty=10,10

#owner
ox=500
rrr=random.randint(0,255)
ggg=random.randint(0,255)
bbb=random.randint(0,255)
pygame.mouse.set_visible(False)


def show_pointer(x,y):
  global pointer_img
  screen.blit(pointer_img,(x-16,y-16))

def is_hit(mouse_x,mouse_y,obj_x,obj_y,obj_width,obj_hight):
  temp=False
  if mouse_x>obj_x+15 and mouse_x<obj_x+obj_width-20:
    if mouse_y>obj_y+13 and mouse_y<obj_y+obj_hight-25:
      temp=True
      if mouse_y>obj_y+27 and mouse_y<obj_y+43:
      	if mouse_x>obj_x+30:
      		temp=False
      if mouse_y<obj_y+30 and mouse_x>obj_y+40:
      	temp=False
    else:
      temp= False
  else:
    temp=False 
  if temp:
  	return True
  else:
  	return False

def show_animal(x,y,pic):
  screen.blit(pic,(x,y))

def show_dead_animal(x,y,t):
  global dead_animal_img
  screen.blit(dead_animal_img[t//100],(x,y))
"""
  s = pygame.Surface((100,100))  # the size of your rect
  s.set_alpha(128)                # alpha level
  s.fill((255,255,255))           # this fills the entire surface
  screen.blit(s, (x,))    # (0,0) are the top-left coordinate
  """
    
def show_score(x,y):
  score_img=font.render("Score :"+str(score),True,(100,100,000))
  screen.blit(score_img,(x,y))
  show_s_gun(x,y)
  bullet_img=font.render(str(bullets_left),True,(250,50,50))
  screen.blit(bullet_img,(x+530,y))

def show_s_gun(x,y):
  if gun_type=="m_gun":
    gun_img=m_gun_img
  else:
    gun_img=handgun_img
  screen.blit(gun_img,(x+470,y-5))

  
def remind_reload():
  pygame.draw.rect(screen, (000,000,000), (screen_width-310, 45, 290, 25))
  reload_img=rfont.render("Press spacebar to Reload ",True,(250,50,250))
  screen.blit(reload_img,(screen_width-300,50))

def show_gun_loading():
  pygame.draw.rect(screen, (000,000,000), (screen_width-310, 45, 290, 25))
  reload_img=rfont.render("Gun Loading... ",True,(250,50,250))
  screen.blit(reload_img,(screen_width-300,50))

def game_over_text():
  over_img=over_font.render("GAME OVER",True,(255,000,000))
  screen.blit(over_img,(screen_width*0.13,screen_high*2/5))
  
running=True

while running:
  screen.fill((0,0,0))
  screen.blit(background,(0,0))
  time.sleep(1/300)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
     
    if event.type== pygame.VIDEORESIZE:
      screen_width=event.w
      screen_high=event.h
      screen=pygame.display.set_mode((screen_width, screen_high),pygame.RESIZABLE)

    if event.type== pygame.MOUSEBUTTONUP:
      if t56_mod:
        t56_mod=False
      fire_ready=True


    if event.type== pygame.KEYDOWN:
      if event.key==pygame.K_SPACE :
        if gun_type=="handgun" and bullets_left<6:
          bullets_left=6
        elif gun_type=="m_gun" and bullets_left<1000:
          bullets_left=1000
        gun_loading_time=30
        gun_load_sound.play(1)

      if event.key==pygame.K_m:
        gun_load_sound.play(1)
        if gun_type=="handgun":
          gun_type="m_gun"
          bullets_left=1000
        elif gun_type=="m_gun":
          gun_type="handgun"
          bullets_left=6
        gun_loading_time=10


      if event.key==pygame.K_z:
        t56_mod=True
      
    if event.type==pygame.KEYUP:
      if event.key==pygame.K_z:
        t56_mod=False


    """    
    if event.type==pygame.KEYUP:
      if event.key==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
        playerx_change = 0*speed
    """
    mouse_x,mouse_y=pygame.mouse.get_pos()
    b1,b2,b3=pygame.mouse.get_pressed()
    if b1:
      if (bullets_left>0 and fire_ready) and gun_loading_time<=0:
        fire_ready=False
        if gun_type=="m_gun":
          t56_sound.play()
          t56_mod=True
        elif gun_type=="handgun":
          bullet_sound.play()
        bullets_left-=1
        time.sleep(1/100)
        for j in range(num_of_animals):
          i=num_of_animals-j-1
          check_hit=is_hit(mouse_x,mouse_y,animal_x[i],animal_y[i],100,100)
          if animal_x[j]>-100 and animal_x[j]<screen_width+150:
            animal_running[j]=300
          if check_hit:
            dead_animal_x.append(animal_x[i])
            dead_animal_y.append(animal_y[i])
            dead_animal_t.append(300)
            animal_x[i]=screen_width+500
            score+=1
            bullet_sound.play()
      else:
        gun_load_sound.play()

  if t56_mod and gun_type=="m_gun":
    if bullets_left>0 and gun_loading_time<=0:
          t56_sound.play()
          bullets_left-=1
          time.sleep(1/100)
          for j in range(num_of_animals):
            i=num_of_animals-j-1
            check_hit=is_hit(mouse_x,mouse_y,animal_x[i],animal_y[i],100,100)
            if animal_x[j]>-100 and animal_x[j]<screen_width+150:
              animal_running[j]=300
            if check_hit:
              dead_animal_x.append(animal_x[i])
              dead_animal_y.append(animal_y[i])
              dead_animal_t.append(300)
              animal_x[i]=screen_width+500
              score+=1
    else:
      gun_load_sound.play()
              

            
  for q in range (len(dead_animal_x)):
    if dead_animal_t[q]>0:
      dead_animal_t[q]-=1
      show_dead_animal(dead_animal_x[q],dead_animal_y[q],dead_animal_t[q])

  qq=len(dead_animal_x)
  for abx in range (qq):
    if dead_animal_t[abx]<0:
      dead_animal_x.pop(abx)
      dead_animal_y.pop(abx)
      dead_animal_t.pop(abx)
      break



  for ii in range (num_of_animals):
    deer_x=animal_x[ii]
    deer_y=animal_y[ii]
    animal_pic_num=animal_img_num[ii]
    deer_pic=animal_img[animal_pic_num]
    temp_num=random.randint(0,10)
    if temp_num==7 :
      animal_img_num[ii]=random.randint(0,1)
    run_id=animal_running[ii]
    if run_id!=0:
      animal_x[ii]-=((run_id//50)+7)
      deer_pic=animal_run_img[run_id%4]
      animal_running[ii]-=1
      
    show_animal(deer_x,deer_y,deer_pic)
    if animal_x[ii]<-500:
      animal_x[ii]=screen_width*1.5
      animal_y[ii]=random.randint(150,260)



  screen.blit(background2,(0,0))     
  show_pointer(mouse_x,mouse_y)
  
  for j in range (num_of_animals):
    temp_num=random.randint(0,100)
    if temp_num==7 :
      animal_running[j]=random.randint(0,80)
      
  if bullets_left==0:
    remind_reload()

  if gun_loading_time>0:
    gun_loading_time-=1
    show_gun_loading()

  #owner
  if ox<-270:
    ox=screen_width
    rrr=random.randint(0,255)
    ggg=random.randint(0,255)
    bbb=random.randint(0,255)
  else:
    ox-=speed
    
  
  show_score(textx,texty)
  creater_img=ofont.render("This Game Created by : (c) TPC - 2020 ",True,(rrr,ggg,bbb))
  screen.blit(creater_img,(ox,screen_high-20))
  pygame.display.update()


pygame.quit() 
