'''
    This program creates a graphics window with a rectangle. It provides
    template used with all of the graphical programs used in the book.
'''

from graphics import GraphicsWindow

# Create the window and access the canvas.
win = GraphicsWindow()
canvas = win.canvas()

# Draw on the canvas.
canvas.drawRect(100, 100, 250, 150)

# Wait for the user to close the window
win.wait()