import PyGUIgame as pgg

# more then 120 isn't accurate nor necessary
win = pgg.init(512,256, "demo window", FPS=120)

# prints all available fonts
print("all available fonts:",pgg.get_fonts())
print("default font:",pgg.get_default_font())

run = True
while run:
		# updates all variables in win (keys,fps,...)
		win.update()

		# fills the background
		win.background(pgg.GRAY)

		# draws a line, rect and circle
		win.draw_line(pgg.WHITE,(10,10),(200,60))
		win.draw_rect(pgg.WHITE, (60,90), (70,50), pgg.HOLLOW)
		win.draw_circle(pgg.WHITE, (30,-54),10,pgg.FILLED)

		# text, fonts, colors and system variables
		# makes a font
		font = pgg.Font("dejavusans",20)

		# makes the text
		hello = pgg.Text("hello world!",font=font)
		otherfont = pgg.Text("this is written in the standard font")

		othercolor = pgg.Text("this is written in another color",color=pgg.BLUE, font=font)
		frame = pgg.Text(f"framecounter: {win.getFrames()}",font=font)
	
		fps = pgg.Text(f"fps: {win.getFPS()}",font=font)
		avfps = pgg.Text(f"av fps: {win.getAvFPS()}",font=font)
	
		gametime = pgg.Text(f"time: {win.getTime()}",font=font)

		# draws the text
		win.draw_text(hello, (-250,120))
		win.draw_text(otherfont, (-250,80))
		win.draw_text(othercolor, (-250,60))
		win.draw_text(frame, (-250,40))
		win.draw_text(fps, (-250,10))
		win.draw_text(avfps, (-250,-20))
		win.draw_text(gametime, (-250,-60))

		# prints mouse pos
		print(win.getMousePos())

		# is key escape is pressed, the programs stops
		if win.isKeyPressed("Escape") or win.QUIT:
			run = False