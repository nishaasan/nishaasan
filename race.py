from turtle import *
from random import randint
#setting up the pen to draw the race track. 
speed(0)
penup()
goto(-140, 140)

#Loop for drawing the race track
for step in range(15):
  #Writing the track line number from 0 to 14
  write(step, align='center')
  right(90)

  # drawing a track line
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)

  # started to draw the next track line. Like wise 15 track line can be drawn
  penup()
  backward(160) # Going top to draw next track line
  left(90)
  forward(20) # Making spaces between two track line

turtle1 = Turtle()
turtle1.color('red')
turtle1.shape('turtle')

turtle1.penup()
turtle1.goto(-160, 100)
turtle1.pendown()

for turn in range(10):
  turtle1.right(36)

turtle2 = Turtle()
turtle2.color('blue')
turtle2.shape('turtle')

turtle2.penup()
turtle2.goto(-160, 70)
turtle2.pendown()

for turn in range(72):
  turtle2.left(5)

turtle3 = Turtle()
turtle3.shape('turtle')
turtle3.color('green')

turtle3.penup()
turtle3.goto(-160, 40)
turtle3.pendown()

for turn in range(60):
  turtle3.right(6)

turtle4 = Turtle()
turtle4.shape('turtle')
turtle4.color('orange')

turtle4.penup()
turtle4.goto(-160, 10)
turtle4.pendown()

for turn in range(30):
  turtle4.left(12)

for turn in range(100):
  turtle1.forward(randint(1,5))
  turtle2.forward(randint(1,5))
  turtle3.forward(randint(1,5))
  turtle4.forward(randint(1,5))
  
