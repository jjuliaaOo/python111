import turtle


def move(s, k):
    t.penup()
    draw(s, k)
    t.pendown()


def draw(s, k):
    x = t.xcor()
    y = t.ycor()
    if s == 'up':
        t.goto(x, y+k)
    elif s == 'down':
        t.goto(x, y-k)
    elif s == 'left':
        t.goto(x-k, y)
    elif s == 'right':
        t.goto(x+k, y)
    elif s == 'rightup':
        t.goto(x+k, y+k)
    elif s == 'rightdown':
        t.goto(x+k, y-k)
    elif s == 'leftup':
        t.goto(x-k, y+k)
    elif s == 'leftdown':
        t.goto(x-k, y-k)


t = turtle.Turtle()
t.shape("turtle")
move('right', 150)

number = int(input('Введите почтовый индекс:'))
p = number
v = 0

while p != 0:
    u = p % 10
    p = p // 10
    v = v+1

if v == 6:
    for i in range (6):
        u = number % 10
        if u == 0:
            draw('up', 40)
            draw('right', 40)
            draw('down', 80)
            draw('left', 40)
            draw('up', 40)
        elif u == 1:
            draw('rightup', 40)
            draw('down', 80)
            move('left', 40)
            move('up', 40)
        elif u == 2:
            move('up', 40)
            draw('right', 40)
            draw('down', 40)
            draw('leftdown', 40)
            draw('right', 40)
            move('left', 40)
            move('up', 40)
        elif u == 3:
            move('up', 40)
            draw('right', 40)
            draw('leftdown', 40)
            draw('right', 40)
            draw('leftdown', 40)
            move('up', 40)
        elif u == 4:
            draw('up', 40)
            move('right', 40)
            draw('down', 80)
            move('up', 40)
            draw('left', 40)
        elif u == 5:
            move('up', 40)
            move('right', 40)
            draw('left', 40)
            draw('down', 40)
            draw('right', 40)
            draw('down', 40)
            draw('left', 40)
            move('up', 40)
        elif u == 6:
            move('up', 40)
            move('right', 40)
            draw('leftdown', 40)
            draw('right', 40)
            draw('down', 40)
            draw('left', 40)
            draw('up', 40)
        elif u == 7:
            move('up', 40)
            draw('right', 40)
            draw('leftdown', 40)
            draw('down', 40)
            move('up', 40)
        elif u == 8:
            draw('up', 40)
            draw('right', 40)
            draw('down', 40)
            draw('left', 40)
            draw('down', 40)
            draw('right', 40)
            draw('up', 40)
            move('left', 40)
        elif u == 9:
            move('right', 40)
            draw('left', 40)
            draw('up', 40)
            draw('right', 40)
            draw('down', 40)
            draw('leftdown', 40)
            move('up', 40)

        number = number // 10
        move('left', 80)
    move('rightdown', 80)
else:
    print('Не индекс! Должно быть 6 цифр, а не ', v, '!', sep='')
turtle.done()
