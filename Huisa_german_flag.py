from graphics import GraphicsWindow

win = GraphicsWindow(300, 300)
canvas = win.canvas()


canvas.setColor("black")
canvas.drawRect(70,70, 140, 30)

# canvas.drawLine(100, 70, 130, 70)

canvas.setColor("red")
canvas.drawRect(70, 100, 140, 30)

canvas.setColor("gold")
canvas.drawRect(70, 130, 140, 30)







