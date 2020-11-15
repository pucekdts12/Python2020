import pygame as pg,numpy as np
from . import BaseScene,MainMenu
import itertools as it
import Elements

#Helper functions
def clamp(val,min_val,max_val):
  return max(min(val,max_val),min_val)

class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y

class Ball(Elements.Ball): #AdvancedBall
  def __init__(self,*args):
    super().__init__(*args)    
    self.const_forces = [[0,0.981]] # siły ze stałym zwrotem oraz zkierunkiem | grawitacje ustawiam 10x mniejsza bo inaczej lata za szybko :)
    self.relative_forces = [[-0.02,-0.02]] # tarcie powietrza i/lub inne siły
    self.friction = -1 # tarcie powierzchni
    self.bounds = [float('-inf'),float('-inf'),float('inf'),float('inf')] # domyślnie brak granic

  def update(self):
    # Apply forces
    for f in self.const_forces:
      self.speed = np.add(self.speed,f)

    for f in self.relative_forces:
      self.speed = np.add(self.speed,np.sign(self.speed)*f)


    self.rect.move_ip(self.speed)

    if self.rect.center[0] < self.bounds[0].x or self.rect.center[0] > self.bounds[1].x:
      self.speed[0]*=-1
      self.speed[0]+= np.sign(self.speed[0])*self.friction

    if self.rect.center[1] < self.bounds[0].y or self.rect.center[1] > self.bounds[1].y:
      self.speed[1]*=-1
      self.speed[1]+= np.sign(self.speed[1])*self.friction
      
    # move to bounds
    self.rect.center = (
      clamp( self.rect.center[0],self.bounds[0].x,self.bounds[1].x ),
      clamp( self.rect.center[1],self.bounds[0].y,self.bounds[1].y )
    )
      
      

    
      



    

class Scene(BaseScene.Scene):
  def __init__(self,screen):
    super().__init__(screen)
    self.size = self.screen.get_rect().size
    self.bg = pg.Surface((screen.get_width(),screen.get_height()))
    self.bg.fill((33,33,33))

    self.ball = Ball(80,(255,0,0))
    self.start_speed = [0,0] # poczatkowa predkosc | jest napisywana jesli zostanie wywolana przez MainMenu
    self.ball.bounds = [Point(40,40),Point(self.screen.get_width()-40,screen.get_height()-40)] # ograniczenia srodka pilki
    self.reset()
    
    
    

  def preEvents(self):
      keys = pg.key.get_pressed()
      if keys[pg.K_ESCAPE]:
        self.next_scene = MainMenu.Scene(self.screen)
        return
      elif keys[pg.K_r]:
        self.reset()

      self.ball.update()
      
      


      self.screen.blit(self.bg,(0,0))
      self.ball.draw(self.screen)
      pg.display.flip()


  def reset(self):
    self.ball.speed = self.start_speed
    self.ball.rect.left = (self.size[0]-self.ball.rect.width)/2
    self.ball.rect.top = (self.size[1]-self.ball.rect.height)/2