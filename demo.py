import PyGUIgame as pgg

win = pgg.init(512,256, "demo window")

run = True
while run:
    win.update()

    win.background(pgg.RED)

    win.draw_line(pgg.WHITE,(10,10),(50,50))

    win.draw_rect(pgg.WHITE, (30,30), (90,90), pgg.HOLLOW)

    win.draw_circle(pgg.WHITE, (100,30),10,pgg.FILLED)

    print(win.getMousePos(), win.getKeysDown(), win.getMousePressed())

    if win.isKeyPressed("Escape"):
      run = False