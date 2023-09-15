import turtle as tur
import math
turtle = tur.Turtle()
i = 0
turtle.shape('turtle')
turtle.speed(10)
for i in range(100):
  turtle.forward(20+i*20)
  turtle.left(90)
  turtle.forward(20+i*20)
  turtle.left(90)
