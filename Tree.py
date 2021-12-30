from turtle import *
import turtle

speed(10)



# Tree Trunk
penup()
goto(-15, -50)
pendown()
color("#6E260E")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()


y = -50
width = 240
height = 25

# Green section of tree 
while width > 20:
    width = width - 30 
    x = 0 - width / 2 
    color("#228B22")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
    
    y = y + height 

# Star
penup()
goto(-15, 150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()

# Popup
penup()
goto(-130, -150)
color("red")
write("MERRY CHRISTMAS", font=("Arial", 20, "bold"))
delay(100)

turtle.setup(500,500)
board = turtle.Turtle()
 
# draws a rectangle given top left position of a rectangle
def draw_rectangle(board,x,y,width,height,size,color):
  board.pencolor(color)
  board.pensize(size)
  board.setheading(0)
 
  board.up()
  board.goto(x,y)
  board.down()
  # draw top
  board.forward(width)
  # draw right
  board.right(90)
  board.forward(height)
  # draw bottom
  board.right(90)
  board.forward(width)
  # draw left
  board.right(90)
  board.forward(height)
  board.end_fill()
 
 

draw_rectangle(board,-160,160,350,340,5,"blue")

draw_rectangle(board,-160,160,340,330,5,"orange")
turtle.done()

hideturtle()