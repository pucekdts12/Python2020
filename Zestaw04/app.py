import pygame as pg
from Scenes import MainMenu

class App:
  @staticmethod
  def main():
    size = (800,600)
    screen = pg.display.set_mode(size)
    pg.font.init()
    running = True
    pg.display.set_caption("Zestaw04")
    
    
    #pygame.mixer.music.load(r'C:\Users\witol\Documents\UJ\PYTHON\GAME\music.mp3')
    #pygame.mixer.music.play(-1)

    active_scene = MainMenu.Scene(screen)
    while running:
        active_scene.preEvents()

        for e in pg.event.get():
          active_scene.eventHandler(e)
          
        active_scene.postEvents()

        if not active_scene.running: break
        if active_scene.next_scene: active_scene = active_scene.next_scene



if __name__=="__main__":
  pg.init()
  App.main()
  pg.quit()
  sys.exit()