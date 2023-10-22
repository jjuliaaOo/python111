import pygame as pg
import sys
from threading import Thread

pg.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
sc = pg.display.set_mode((500, 400))
sc.fill(BLUE)

r = 20

def blick(x, r):
    while r < 500:
        pg.draw.circle(sc, WHITE, x, r, 2)
        pg.display.flip()
        kadr.tick(30)
        pg.draw.circle(sc, BLUE, x, r, 2)
        r = r + 10


kadr = pg.time.Clock()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
            blick(i.pos, 20)
