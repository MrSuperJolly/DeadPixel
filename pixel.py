import turtle



colourPos = 0


def right():
        global colourPos
        if colourPos > 0:
                colourPos = colourPos - 1
               

def left():
        global colourPos
        if colourPos <= 4:
                colourPos = colourPos + 1
                



win = turtle.Screen()
win.title("Dead Pixel")
win.setup(width = 1.0, height = 1.0)


colours = ["black", "white", "yellow", "blue", "green", "red"]


win.listen()
win.onkeypress(left, "a")
win.onkeypress(right, "d")

while True:
    win.update()
    win.bgcolor(colours[colourPos])
    
   




