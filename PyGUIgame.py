import pygame
pygame.init()


FILLED = False
HOLLOW = True

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


def init(width, height, name):
  return pggWindow(width, height, name)

class pggWindow:
  def __init__(self, width, height, name):
    self.width = width
    self.height = height
    self.name = name

    self.win = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption(name)

    self.keys = []
    self.mouseButtons = []
    self.pos = 0,0

    self.mousedown = False
    self.mouseup = False

  def Update(self):
    pygame.display.update()
    self.win.fill((0,0,0))

    self.pos = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed(num_buttons=3)
    self.mouseButtons = [buttons[0], buttons[2]]

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        self.keys.append(event.key)
      if event.type == pygame.KEYUP:
        if event.key in self.keys:
          self.keys.remove(event.key)
          
      self.mousedown = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.mousedown = True
      self.mouseup = False
      if event.type == pygame.MOUSEBUTTONUP:
        self.mouseup = True

  def background(self, color):
    self.win.fill(color)

  def draw_line(self, color, p1, p2):
    pygame.draw.line(self.win, color, p1, p2)
  def draw_rect(self, color, p1, p2, filled=False):
    pygame.draw.rect(self.win, color, (p1, p2), filled)
  def draw_circle(self, color, p, r, filled=False):
    pygame.draw.circle(self.win, color, p, r, filled)


if __name__ == "__main__":
  print("this is a demo")
  win = init(512,256,"DemoWindow")
  
  run = True
  while run:
    win.Update()
    win.background(RED)
    win.draw_line(WHITE,(10,10),(50,50))
    win.draw_rect(WHITE, (30,30), (90,90), HOLLOW)
    win.draw_circle(WHITE, (100,30),10,FILLED)
    print(win.pos, win.keys, win.mouseButtons)