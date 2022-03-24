import pygame
pygame.init()


FILLED = False
HOLLOW = True

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_GRAY = (200,200,200)
GRAY = (120,120,120)
DARK_GRAY = (50,50,50)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

keycodes = {}

keycodes.update({
	27:"Escape",
	1073741906:"Up",
	1073741905:"Down",
	1073741904:"Left",
	1073741903:"Right",
	1073742049:"LShift",
	1073742053:"RShift",
	1073742048:"LCtrl",
	1073742052:"RCtrl",
	1073742050:"Alt",
	32:"Space",
	13:"Enter",
	8:"Backspace",
	9:"Tab"
	})
for i in range(49,58):
	keycodes[i] = str(i-48)
keycodes[48] = "0"
for i in range(97,123):
	keycodes[i] = chr(i)



def init(width, height, name, FPS=60):
	return pggWindow(width, height, name, FPS)

def get_fonts():
	return pygame.font.get_fonts() + ["freesansbold", "arial", "aerial"]
def get_default_font():
	return pygame.font.get_default_font().split(".")[0]

class Font:
	def __init__(self,fontname,size):
		self.Font = pygame.font.SysFont(fontname, size)

class Text:
	def __init__(self,text,color=(0,0,0),font=Font(get_default_font(),20)):
		self.__Text = font.Font.render(text, True, color)
		self.__width = self.__Text.get_width()
		self.__height = self.__Text.get_height()
	def getWidth(self):
		return self.__width
	def getHeight(self):
		return self.__height
	def getText(self):
		return self.__Text

class pggWindow:
	def __init__(self, width, height, name, FPS):
		self.__width = width
		self.__height = height
		self.__name = name

		self.__SetFPS = FPS
		self.__FPS = 0
		self.__AvFPS = 0
		self.__Time = 0
		self.__Frames = 0

		self.__Clock = pygame.time.Clock()

		self.__win = pygame.display.set_mode((self.__width, self.__height))
		pygame.display.set_caption(self.__name)

		self.__QUIT = False
		self.QUIT = False

		self.__keys = []
		self.__mouseButtons = []
		self.__pos = 0,0

		self.__mouseDownEvent = False
		self.__mouseUpEvent = False
		self.__keyDownsEvent = []

	def __translate_pyg_pgg(self, pos):
		return pos[0]-self.__width/2, (self.__height-pos[1])-self.__height/2
	def __translate_pgg_pyg(self, pos):
		return pos[0]+self.__width/2, -pos[1]-self.__height/2+self.__height

	def getWidth(self):
		return self.__width
	def getHeight(self):
		return self.__height
	def getName(self):
		return self.__name

	def getSetFPS(self):
		return self.__SetFPS
	def getFPS(self):
		return round(self.__FPS,2)
	def getAvFPS(self):
		return round(self.__AvFPS,2)
	def getTime(self):
		return self.__Time
	def getFrames(self):
		return self.__Frames

	def isKeyDown(self, keycode):
		if keycode in self.__keys:
			return True
		return False
	def getKeysDown(self):
		return self.__keys

	def getMousePos(self):
		return self.__translate_pyg_pgg(self.__pos)
	def getMousePressed(self):
		return self.__mouseButtons
	def getLeftMouse(self):
		return self.__mouseButtons[0]
	def getRightMouse(self):
		return self.__mouseButtons[1]
	
	def MouseDown(self):
		return self.__mouseDownEvent
	def MouseUp(self):
		return self.__mouseUpEvent
	def getKeysPressed(self):
		return self.__keysDownEvent
	def isKeyPressed(self, keycode):
		if keycode in self.__keysDownEvent:
			return True
		return False


	def update(self):

		pygame.display.update()
		self.__Clock.tick(self.__SetFPS)
		self.__FPS = self.__Clock.get_fps()
		self.__Time = pygame.time.get_ticks()/1000
		self.__Frames += 1
		if self.__Time % 1 > 1 - 1/self.__SetFPS:
			self.__AvFPS = self.__FPS

		self.__win.fill((0,0,0))

		self.__pos = pygame.mouse.get_pos()
		
		self.__mouseButtons = [pygame.mouse.get_pressed(num_buttons=3)]

		self.__keysDownEvent = []
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.__QUIT = True
			if event.type == pygame.KEYDOWN:
				if event.key in keycodes:
					self.__keys.append(keycodes[event.key])
					self.__keysDownEvent.append(keycodes[event.key])
				else:
					self.__keys.append(event.key)
					self.__keysDownEvent.append(event.key)
			if event.type == pygame.KEYUP:
				if event.key in keycodes:
					if keycodes[event.key] in self.__keys:
						self.__keys.remove(keycodes[event.key])
				elif event.key in self.__keys:
					self.__keys.remove(event.key)
					
			self.__mouseDown = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.__mouseDown = True
			self.__mouseUp = False
			if event.type == pygame.MOUSEBUTTONUP:
				self.__mouseUp = True
				
		self.QUIT = self.__QUIT

	def background(self, color):
		self.__win.fill(color)

	def draw_line(self, color, p1, p2):
		pygame.draw.line(self.__win, color, self.__translate_pgg_pyg(p1), self.__translate_pgg_pyg(p2))
	# takes in a point from where to start and the dimensions of the rectangle
	def draw_rect(self, color, p, dim, filled=False):
		pygame.draw.rect(self.__win, color, (self.__translate_pgg_pyg(p), dim), filled)
	def draw_circle(self, color, p, r, filled=False):
		pygame.draw.circle(self.__win, color, self.__translate_pgg_pyg(p), r, filled)
	def draw_text(self, text, p):
		self.__win.blit(text.getText(), self.__translate_pgg_pyg(p))





#------
# demo
#------
if __name__ == "__main__":
	print("this is a demo")
	win = init(512,256,"DemoWindow")
	
	run = True
	while run:
		win.update()
		win.background(RED)
		win.draw_line(WHITE,(10,10),(50,50))
		win.draw_rect(WHITE, (30,30), (90,90), HOLLOW)
		win.draw_circle(WHITE, (100,30),10,FILLED)
		print(win.pos, win.keys, win.mouseButtons)