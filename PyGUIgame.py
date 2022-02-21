import pygame
pygame.init()

class pggWindow:
  def __init__(self,
  width=256,
  height=128,
  name="PyGUIgame window"):

    self.width = width
    self.height = height
    self.name = name
    self.isDefined = False

    self.keys = []
    self.mouseButtons = []
    self.pos = 0,0

  def Update(self):
    self.pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        self.keys.append(event.key)
      if event.type == pygame.KEYUP:
        if event.key in self.keys:
          self.keys.remove(event.key)

Window = pggWindow()

def GetWindow(width, height, name=""):
  if Window.isDefined == True:
    raise Exception("There Can Only be 1 window!")
  if name != "":
    Window.name = name
  Window.width = width
  Window.height = height
  Window.isDefined = True
  return Window

if __name__ == "__main__":
  print("this is a demo")
  win = GetWindow(100,50,"DemoWindow")
  
  run = True
  while run:
    win.Update()