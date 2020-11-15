import pygame as pg,numpy as np
from . import BaseScene,MainMenu
import Elements

class Ball(Elements.Ball):
  def __init__(self,*args):
    super().__init__(*args)
    self.forces = []
    self.bounds = []

  def update(self):
    for f in self.forces: #apply forces
      self.speed = np.add(self.speed,f)


    self.rect.move_ip(self.speed)

    if self.rect.bottom > self.bounds[3]:
      self.speed[1]*=-1



    

class Scene(BaseScene.Scene):
  def __init__(self,screen):
    super().__init__(screen)
    self.size = self.screen.get_rect().size
    self.bg = pg.Surface((screen.get_width(),screen.get_height()))
    self.bg.fill((33,33,33))

    self.ball = Ball(80,(255,0,0))
    self.start_speed = [0,0] # poczatkowa predkosc | jest napisywana jesli zostanie wywolana przez MainMenu
    self.ball.velocity = [0,0] 
    self.ball.forces = [[0,0.981]] # ustawiam 10x mniejsza bo inaczej lata za szybko :)
    self.ball.forces = [[0,1]]
    self.ball.bounds = [0,0,self.screen.get_width(),screen.get_height()]
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