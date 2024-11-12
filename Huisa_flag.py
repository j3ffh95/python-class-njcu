from graphics import GraphicsWindow

win = GraphicsWindow(300, 300)
canvas = win.canvas()

xLeft = 10
yTop = 10
width = 30
height = 60


canvas.setColor("green")
canvas.drawRect(70,70, 30, 60)

canvas.drawLine(100, 70, 130, 70)

canvas.setColor("white")
canvas.drawRect(100, 70, 30, 60)

canvas.setColor("red")
canvas.drawRect(130, 70, 30, 60)


