import pygame as pg
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
