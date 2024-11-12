from graphics import GraphicsWindow

# Create the window and access the canvas
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw on the canvas.
canvas.setColor("#0b7a75")
canvas.drawRect(0, 10, 350, 40)

canvas.setColor("#d7c9aa")
canvas.drawRect(0, 70, 100, 40)

canvas.setColor("#7b2d26")
canvas.drawRect(0, 130, 200, 40)

# Wait for the user to close the window.
win.wait()