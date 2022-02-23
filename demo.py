import PyGUIgame as pgg

# more then 120 isn't accurate nor necessary
win = pgg.init(512,256, "demo window", FPS=120)

run = True
while run:
    win.update()

    win.background(pgg.RED)

    win.draw_line(pgg.WHITE,(350,10),(500,50))
    win.draw_rect(pgg.WHITE, (350,50), (100,90), pgg.HOLLOW)
    win.draw_circle(pgg.WHITE, (400,160),10,pgg.FILLED)

    font = pgg.Font("freesansbold.ttf",15)

    hello = pgg.Text("hello world!")
    otherfont = pgg.Text("this is written in another font",font=font)
    othercolor = pgg.Text("this is written in another color",color=pgg.BLUE)
    frame = pgg.Text(f"framecounter: {win.getFrames()}",font=font)
    fps = pgg.Text(f"fps: {win.getFPS()}",font=font)
    avfps = pgg.Text(f"av fps: {win.getAvFPS()}",font=font)
    gametime = pgg.Text(f"time: {win.getTime()}",font=font)
    win.draw_text(hello, (10,10))
    win.draw_text(otherfont, (10,50))
    win.draw_text(othercolor, (10,70))
    win.draw_text(frame, (10,90))
    win.draw_text(fps, (10,120))
    win.draw_text(avfps, (10,150))
    win.draw_text(gametime, (10,190))

    #print(win.getMousePos(), win.getKeysDown(), win.getMousePressed())

    if win.isKeyPressed("Escape"):
      run = False