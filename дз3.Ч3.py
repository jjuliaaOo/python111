from random import randint
import random
import math
import turtle

num_turtles = 15
st = 100
turtle_speed = 10000000

turtles=[]
arr=[]
m=[]
x=10
f=10
j=0
k=0
for i in range(num_turtles):
  new_turtle = turtle.Turtle()
  new_turtle.shape(name='turtle')
  turtles.append(new_turtle)

for turtle in turtles:
  turtle.penup()
  turtle.speed(turtle_speed)
  b=[]
  c=[]
  for d in range (-x, x+1, 2):
    b.append(d)
    c.append(math.sqrt(x**2-d**2))
  for d in range (x, -x-1, -5):
    b.append(d)
    c.append(-math.sqrt(x**2-d**2))

arr.append(b)
arr.append(c)
m.append(randint(0,len(c)-1))
turtle.goto(arr[j][m[k]], arr[j+1][m[k]])
k=k+1
j=j+2
x=x+15

for i in range(1000):
  h=0
  t=0
  for turtle in turtles:
    turtle.pendown()
    turtle.goto(arr[h][m[t]], arr[h+1][m[t]])
    if m[t]<len(arr[h])-1:
      m[t]+=1
    else:
      m[t]=0
    h=h+2
    t=t+1
