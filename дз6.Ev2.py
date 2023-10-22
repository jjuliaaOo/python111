import pygame as pg
import math
import random

pg.init()

sc = pg.display.set_mode((600, 400))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (175, 43, 30)
GREEN = (37, 194, 100)
YELLOW = (201, 178, 58)
YELLOW2 = (204, 174, 24)
GREY = (107, 100, 91)

sc.fill(WHITE)

pg.draw.rect(sc, BLACK, (449, 49, 22, 302))
pg.draw.rect(sc, WHITE, (450, 50, 20, 300))
for i in range (0, 15):
    pg.draw.rect(sc, BLACK, (450, 50+20*i, 10, 10))
for i in range (0, 15):
    pg.draw.rect(sc, BLACK, (460, 60+20*i, 10, 10))

tar1 = pg.draw.circle(sc, ORANGE, [50, 80], 15)
tar2 = pg.draw.circle(sc, ORANGE, [50, 140], 15)
tar3 = pg.draw.circle(sc, ORANGE, [50, 200], 15)
tar3 = pg.draw.circle(sc, ORANGE, [50, 260], 15)
tar4 = pg.draw.circle(sc, ORANGE, [50, 320], 15)

pg.display.flip()

kadr = pg.time.Clock()

sp1 = random.randint(1,10)
sp2 = random.randint(1,10)
sp3 = random.randint(1,10)
sp4 = random.randint(1,10)
sp5 = random.randint(1,10)

x1 = 50
x2 = 50
x3 = 50
x4 = 50
x5 = 50

t = 0
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
            while x1<449 and x2<449 and x3<449 and x4<449 and x5<449:

                pg.draw.circle(sc, WHITE, [x1, 80], 15)
                pg.draw.circle(sc, WHITE, [x2, 140], 15)
                pg.draw.circle(sc, WHITE, [x3, 200], 15)
                pg.draw.circle(sc, WHITE, [x4, 260], 15)
                pg.draw.circle(sc, WHITE, [x5, 320], 15)

                kadr.tick(30)

                x1 = x1 + sp1
                x2 = x2 + sp2
                x3 = x3 + sp3
                x4 = x4 + sp4
                x5 = x5 + sp5

                pg.draw.circle(sc, ORANGE, [x1, 80], 15)
                pg.draw.circle(sc, ORANGE, [x2, 140], 15)
                pg.draw.circle(sc, ORANGE, [x3, 200], 15)
                pg.draw.circle(sc, ORANGE, [x4, 260], 15)
                pg.draw.circle(sc, ORANGE, [x5, 320], 15)
                pg.display.flip()

        if x1 >= 449:
            print('HELLO')
            pg.draw.circle(sc, YELLOW, [500, 80], 8) #медаль
            pg.draw.polygon(sc, (255, 0, 0), [[500, 72], [504, 62], [496, 62]])

        if x2 >= 449:
            print('HELLO')
            pg.draw.circle(sc, YELLOW, [500, 140], 8) #медаль
            pg.draw.polygon(sc, (255, 0, 0), [[500, 132], [504, 122], [496, 122]])

        if x3 >= 449:
            print('HELLO')
            pg.draw.circle(sc, YELLOW, [500,200], 8) #медаль
            pg.draw.polygon(sc, (255, 0, 0), [[500, 192], [504, 182], [496, 182]])

        if x4 >= 449:
            print('HELLO')
            pg.draw.circle(sc, YELLOW, [500, 260], 8) #медаль
            pg.draw.polygon(sc, (255, 0, 0), [[500, 252], [504, 242], [496, 242]])

        if x5 >= 449:
            print('HELLO')
            pg.draw.circle(sc, YELLOW, [500, 320], 8) #медаль
            pg.draw.polygon(sc, (255, 0, 0), [[500, 312], [504, 302], [496, 302]])
        pg.display.flip()




pg.display.flip()
