import pygame as pg
from . import BaseScene,MainMenu
from Elements import Ball

class Scene(BaseScene.Scene):
  def __init__(self,screen):
    super().__init__(screen)
    self.bg = pg.Surface((screen.get_width(),screen.get_height()))
    self.bg.fill((33,33,33))
    self.ball = Ball(80,(255,0,0))
    self.size = self.screen.get_rect().size
    self.ball.rect.left=(screen.get_width()-self.ball.rect.width)/2
    self.ball.rect.top=(screen.get_height()-self.ball.rect.height)/2
    self.size = screen.get_rect().size
    self.speed_step = 0.1

  def preEvents(self):
      keys = pg.key.get_pressed()
      if keys[pg.K_ESCAPE]:
        self.next_scene = MainMenu.Scene(self.screen)
        return
      #ruch dziala jak w grze asteroidy
      if keys[pg.K_UP]:
        self.ball.speed[1] = round(self.ball.speed[1]-self.speed_step,2)
      if keys[pg.K_RIGHT]:
        self.ball.speed[0] = round(self.ball.speed[0]+self.speed_step,2)
      if keys[pg.K_DOWN]:
        self.ball.speed[1] = round(self.ball.speed[1]+self.speed_step,2)
      if keys[pg.K_LEFT]:
        self.ball.speed[0] = round(self.ball.speed[0]-self.speed_step,2)
      if keys[pg.K_r]:
        self.ball.speed=[0,0]
        self.ball.rect.left=(self.size[0]-self.ball.rect.width)/2
        self.ball.rect.top=(self.size[1]-self.ball.rect.height)/2

      self.ball.move()

      if self.ball.rect.left<0 or self.ball.rect.right>self.size[0]:
        self.ball.speed[0]*=-1
      if self.ball.rect.top<0 or self.ball.rect.bottom>self.size[1]:
        self.ball.speed[1]*=-1

      self.screen.blit(self.bg,(0,0))
      self.ball.draw(self.screen)
      pg.display.flip()