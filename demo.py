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
		win.draw_line(pgg.WHITE,(350,10),(500,50))
		win.draw_rect(pgg.WHITE, (350,50), (100,90), pgg.HOLLOW)
		win.draw_circle(pgg.WHITE, (400,160),10,pgg.FILLED)

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
		win.draw_text(hello, (10,10))
		win.draw_text(otherfont, (10,50))
		win.draw_text(othercolor, (10,70))
		win.draw_text(frame, (10,90))
		win.draw_text(fps, (10,120))
		win.draw_text(avfps, (10,150))
		win.draw_text(gametime, (10,190))

		# is key escape is pressed, the programs stops
		if win.isKeyPressed("Escape") or win.QUIT:
			run = False