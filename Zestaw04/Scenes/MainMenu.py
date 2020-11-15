import pygame as pg
from Elements import Ball,Label,Button
from . import BaseScene,Zadanie1,Zadanie2

class Scene(BaseScene.Scene):
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
        self.next_scene = Zadanie1.Scene(self.screen)
      elif self.btn_zad2.rect.collidepoint(pos):
        self.next_scene = Zadanie2.Scene(self.screen)
        self.next_scene.start_speed = self.start_speed
        self.next_scene.reset()
        
    return True