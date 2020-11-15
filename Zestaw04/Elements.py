import pygame as pg
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