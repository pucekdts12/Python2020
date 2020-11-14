import pygame as pg,sys
import numpy as np


class Ball:
  def __init__(self,r,color):
    self.surface = pg.Surface((r,r),pg.SRCALPHA,32).convert_alpha()
    self.surface.fill((0,0,0,0))
    self.rect = self.surface.get_rect(center=(r/2,r/2))
    self.speed=[0,0]
    self.velocity=[0,0]
    pg.draw.circle(self.surface,color,(r/2,r/2),r/2)

  def s(self):
    return self.surface

  def move(self):
    self.rect.move_ip(self.speed)

  
    
    
    


  def draw(self,surface):    
    surface.blit(self.s(),self.rect)

class Label:
  def __init__(self,text,ff,color,bgc=None):
    if bgc==None: bgc=(0,0,0,0)
    self.surf = ff.render(text,False,color)
    self.rect = self.surf.get_rect()
    bg = pg.Surface(self.rect.size,pg.SRCALPHA,32).convert_alpha()
    bg.fill(bgc)
    bg.blit(self.surf,(0,0))
    self.surf = bg

  def draw(self,screen):
    screen.blit(self.surf,self.rect)

class Button(Label):
  def __init__(self,text,ff,color,bgc=None):
    super().__init__(text,ff,color,bgc)
  

class Scene:
  def __init__(self,screen):
    self.screen = screen
    self.clock = pg.time.Clock()
    self.running = True
    self.next_scene = None

  def preEvents(self):
    pass

  def eventHandler(self,e):
    if e.type==pg.QUIT:
      self.running = False
      return True
    
  def switchScene(self,scene):
    self.next_scene = scene

  def postEvents(self):
    self.clock.tick(60)


class Scene_MainMenu(Scene):
  def __init__(self,screen):
    super().__init__(screen)
    self.bg = pg.Surface(screen.get_rect().size)
    self.bg.fill((33,33,33))
    self.ff = ff = pg.font.SysFont('Arial',30)

    #self.text = self.ff.render('Hello World!!!',False,(0,255,0))
    font_color = (0,200,255)

    self.btn_zad1 = Button('Zadanie 1',ff,font_color)
    self.btn_zad1.rect.center = (screen.get_width()/2,80)

    self.btn_zad2 = Button('Zadanie 2',ff,font_color)
    self.btn_zad2.rect.center = (screen.get_width()/2,160)
    self.label_Speed = Label('Start Speed:',ff,(255,255,255))
    self.start_speed=[0,0]
    self.label_Speed.rect.center = (screen.get_width()/2,200)
    self.label_SpeedVal = Label(str(self.start_speed),ff,(255,0,0))
    self.label_SpeedVal.rect.center = (screen.get_width()/2,240)
    


  def preEvents(self):
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
      self.start_speed[1] = round(self.start_speed[1]+0.1,2)
    elif keys[pg.K_RIGHT]:
      self.start_speed[0] = round(self.start_speed[0]+0.1,2)
    elif keys[pg.K_DOWN]:
      self.start_speed[1] = round(self.start_speed[1]-0.1,2)
    elif keys[pg.K_LEFT]:
      self.start_speed[0] = round(self.start_speed[0]-0.1,2)
    elif keys[pg.K_r]:
      self.start_speed=[0,0]

    self.label_SpeedVal = Label(str(self.start_speed),self.ff,(255,0,0))
    self.label_SpeedVal.rect.center = (self.screen.get_width()/2,240)

    self.screen.blit(self.bg,(0,0))
    
    self.btn_zad1.draw(self.screen)
    self.btn_zad2.draw(self.screen)
    self.label_Speed.draw(self.screen)
    self.label_SpeedVal.draw(self.screen)
    pg.display.flip()

  def eventHandler(self,e):
    if super().eventHandler(e):
      return
    if e.type==pg.MOUSEBUTTONUP:
      pos = pg.mouse.get_pos()
      if self.btn_zad1.rect.collidepoint(pos):
        self.next_scene = Scene_Zad1(self.screen)
      elif self.btn_zad2.rect.collidepoint(pos):
        self.next_scene = Scene_Zad2(self.screen)
        self.next_scene.start_speed = self.start_speed
        self.next_scene.reset()
        
    return True

class Scene_Zad1(Scene):
  def __init__(self,screen):
    super().__init__(screen)
    self.bg = pg.Surface((screen.get_width(),screen.get_height()))
    self.bg.fill((33,33,33))
    self.ball = Ball(80,(255,0,0))
    self.ball.rect.left=(screen.get_width()-self.ball.rect.width)/2
    self.ball.rect.top=(screen.get_height()-self.ball.rect.height)/2
    self.size = screen.get_rect().size

  def preEvents(self):
      keys = pg.key.get_pressed()
      if keys[pg.K_ESCAPE]:
        self.next_scene = Scene_MainMenu(self.screen)
        return
      if keys[pg.K_UP]:
        self.ball.speed[1]-=0.1
      elif keys[pg.K_RIGHT]:
        self.ball.speed[0]+=0.1
      elif keys[pg.K_DOWN]:
        self.ball.speed[1]+=0.1
      elif keys[pg.K_LEFT]:
        self.ball.speed[0]-=0.1
      elif keys[pg.K_r]:
        self.ball.speed=[0,0]
        self.ball.rect.left=(size[0]-ball.rect.width)/2
        self.ball.rect.top=(size[1]-ball.rect.height)/2

      
      self.ball.speed = np.add(self.ball.speed,self.ball.velocity)

      self.ball.move()
      if self.ball.rect.left<0 or self.ball.rect.right>self.size[0]:
        self.ball.speed[0]*=-1
      if self.ball.rect.top<0 or self.ball.rect.bottom>self.size[1]:
        self.ball.speed[1]*=-1

      self.screen.blit(self.bg,(0,0))
      self.ball.draw(self.screen)
      pg.display.flip()


class Scene_Zad2(Scene):
  def __init__(self,screen):
    super().__init__(screen)
    self.bg = pg.Surface((screen.get_width(),screen.get_height()))
    self.bg.fill((33,33,33))
    self.ball = Ball(80,(255,0,0))
    self.ball.rect.left=(screen.get_width()-self.ball.rect.width)/2
    self.ball.rect.top=(screen.get_height()-self.ball.rect.height)/2
    self.size = self.screen.get_rect().size
    self.start_speed = [0,0] # poczatkowa predkosc
    self.ball.speed = self.start_speed 
    self.ball.velocity = [0,0.981] # ustawiam 10x mniejsza bo inaczej lata za szybko :)
    #self.ball.velocity = [0,9.81]
    self.reset()

  def preEvents(self):
      keys = pg.key.get_pressed()
      if keys[pg.K_ESCAPE]:
        self.next_scene = Scene_MainMenu(self.screen)
        return
      elif keys[pg.K_r]:
        self.reset()

      
      self.ball.speed = np.add(self.ball.speed,self.ball.velocity)

      self.ball.move()

      if self.ball.rect.left<0 or self.ball.rect.right>self.size[0]:
        self.ball.speed[0]*=-1
      if self.ball.rect.top<0 or self.ball.rect.bottom>self.size[1]:
        self.ball.speed[1]*=-1

      bounds = [0,0,self.screen.get_width(),self.screen.get_height()]
      if self.ball.rect.left <= bounds[0]: self.ball.rect.left=bounds[0]
      if self.ball.rect.top <= bounds[1]: self.ball.rect.top=bounds[1]
      if self.ball.rect.right >= bounds[2]: self.ball.rect.right=bounds[2]
      if self.ball.rect.bottom >= bounds[3]: self.ball.rect.bottom=bounds[3]

      self.screen.blit(self.bg,(0,0))
      self.ball.draw(self.screen)
      pg.display.flip()

  def reset(self):
    self.ball.speed = self.start_speed
    self.ball.rect.left = (self.size[0]-self.ball.rect.width)/2
    self.ball.rect.top = (self.size[1]-self.ball.rect.height)/2

  

def main():
  size = (800,600)
  screen = pg.display.set_mode(size)
  pg.font.init()
  running = True
  pg.display.set_caption("Zestaw04")
  
  
  #pygame.mixer.music.load(r'C:\Users\witol\Documents\UJ\PYTHON\GAME\music.mp3')
  #pygame.mixer.music.play(-1)

  active_scene = Scene_MainMenu(screen)
  while running:
      active_scene.preEvents()

      for e in pg.event.get():
        active_scene.eventHandler(e)
        
      active_scene.postEvents()

      if not active_scene.running: break
      if active_scene.next_scene: active_scene = active_scene.next_scene


    


if __name__=="__main__":
  pg.init()
  main()
  pg.quit()
  sys.exit()

