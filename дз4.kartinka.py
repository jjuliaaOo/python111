import pygame as pg
import math

pg.init()
j = 1.05

sc = pg.display.set_mode((500*j, 600*j))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (103, 202, 224)
GREEN = (37, 194, 100)
YELLOW = (201, 178, 58)
YELLOW2 = (204, 174, 24)
GREY = (107, 100, 91)

sc.fill(LIGHT_BLUE)

#фон
pg.draw.rect(sc, YELLOW, (0*j, 100*j, 500*j, 240*j))
for i in range (1, 15):
    pg.draw.line(sc, BLACK, [(0+i*35.7142857)*j, 100*j], [(0+i*35.7142857)*j, 340*j])
pg.draw.rect(sc, GREEN, (0*j, 340*j, 500*j, 260*j))
pg.draw.line(sc, BLACK, [0*j, 340*j], [500*j, 340*j])

#будка
pg.draw.polygon(sc, YELLOW,
                    [[330*j, 380*j], [420*j, 398*j],
                     [420*j, 520*j], [330*j, 470*j]])
pg.draw.polygon(sc, BLACK,
                    [[330*j, 380*j], [420*j, 398*j],
                     [420*j, 520*j], [330*j, 470*j]], 1)
pg.draw.polygon(sc, YELLOW,
                    [[420*j, 398*j], [420*j, 520*j],
                     [455*j, 470*j], [455*j, 370*j]])
pg.draw.polygon(sc, BLACK,
                    [[420*j, 398*j], [420*j, 520*j],
                     [455*j, 470*j], [455*j, 370*j]], 1)
pg.draw.polygon(sc, YELLOW2, [[420*j, 398*j], [330*j, 380*j], [375*j, 310*j]])
pg.draw.lines(sc, BLACK, True,
                  [[420*j, 398*j], [330*j, 380*j], [375*j, 310*j]], 1)
pg.draw.polygon(sc, YELLOW2,
                    [[420*j, 398*j], [375*j, 310*j],
                     [410*j, 290*j], [455*j, 370*j]])
pg.draw.polygon(sc, BLACK,
                    [[420*j, 398*j], [375*j, 310*j],
                     [410*j, 290*j], [455*j, 370*j]], 1)
pg.draw.ellipse(sc, BLACK, [350*j, 415*j, 45*j, 55*j])


#цепь
pg.draw.ellipse(sc, BLACK, [346*j, 463*j, 18*j, 8*j], 1)
pg.draw.ellipse(sc, BLACK, [334*j, 470*j, 18*j, 16*j], 1)
pg.draw.ellipse(sc, BLACK, [324*j, 480*j, 20*j, 10*j], 1)
pg.draw.ellipse(sc, BLACK, [319*j, 484*j, 12*j, 12*j], 1)
pg.draw.ellipse(sc, BLACK, [292*j, 489*j, 32*j, 10*j], 1)
pg.draw.ellipse(sc, BLACK, [279*j, 491*j, 19*j, 10*j], 1)
pg.draw.ellipse(sc, BLACK, [260*j, 492*j, 25*j, 4*j], 1)
pg.draw.ellipse(sc, BLACK, [250*j, 486*j, 16*j, 18*j], 1)
pg.draw.ellipse(sc, BLACK, [237*j, 496*j, 23*j, 8*j], 1)
pg.draw.ellipse(sc, BLACK, [224*j, 500*j, 24*j, 11*j], 1)

#гвоздь
pg.draw.ellipse(sc, GREY, [341*j, 465*j, 10*j, 13*j])
pg.draw.ellipse(sc, BLACK, [341*j, 465*j, 10*j, 13*j], 1)

#тело_собака
pg.draw.ellipse(sc, GREY, [175*j, 475*j, 46*j, 53*j])
pg.draw.ellipse(sc, GREY, [120*j, 450*j, 87*j, 47*j])
pg.draw.ellipse(sc, GREY, [50*j, 460*j, 120*j, 69*j])
pg.draw.ellipse(sc, GREY, [38*j, 489*j, 38*j, 74*j])
pg.draw.ellipse(sc, GREY, [105*j, 502*j, 38*j, 74*j])
pg.draw.ellipse(sc, GREY, [30*j, 558*j, 39*j, 15*j])
pg.draw.ellipse(sc, GREY, [97*j, 572*j, 36*j, 15*j])
pg.draw.ellipse(sc, GREY, [118*j, 448*j, 38*j, 30*j])
pg.draw.ellipse(sc, GREY, [158*j, 490*j, 16*j, 46*j])
pg.draw.ellipse(sc, GREY, [207*j, 512*j, 16*j, 46*j])
pg.draw.ellipse(sc, GREY, [143*j, 532*j, 26*j, 13*j])
pg.draw.ellipse(sc, GREY, [192*j, 554*j, 26*j, 13*j])

#голова_собака
pg.draw.rect(sc, GREY, (43*j, 435*j, 65*j, 70*j))
pg.draw.rect(sc, BLACK, (43*j, 435*j, 65*j, 70*j), 1)
pg.draw.ellipse(sc, GREY, [32*j, 435*j, 20*j, 24*j])
pg.draw.ellipse(sc, BLACK, [32*j, 435*j, 20*j, 24*j], 1)
pg.draw.ellipse(sc, GREY, [98*j, 435*j, 20*j, 24*j])
pg.draw.ellipse(sc, BLACK, [98*j, 435*j, 20*j, 24*j], 1)

#глаза_рот_собака
pg.draw.ellipse(sc, WHITE, [54*j, 461*j, 16*j, 6*j])
pg.draw.ellipse(sc, BLACK, [54*j, 461*j, 16*j, 6*j], 1)
pg.draw.ellipse(sc, WHITE, [80*j, 461*j, 16*j, 6*j])
pg.draw.ellipse(sc, BLACK, [80*j, 461*j, 16*j, 6*j], 1)
pg.draw.ellipse(sc, BLACK, [85*j, 461*j, 6*j, 6*j])
pg.draw.ellipse(sc, BLACK, [59*j, 461*j, 6*j, 6*j])
pg.draw.arc(sc, BLACK, [55*j, 485*j, 40*j, 22*j], 0, math.pi)
pg.draw.polygon(sc, WHITE, [[56*j, 490*j], [59*j, 479*j], [61*j, 486*j]])
pg.draw.polygon(sc, BLACK, [[56*j, 490*j], [59*j, 479*j], [61*j, 486*j]], 1)
pg.draw.polygon(sc, WHITE, [[93*j, 490*j], [90*j, 479*j], [87*j, 486*j]])
pg.draw.polygon(sc, BLACK, [[93*j, 490*j], [90*j, 479*j], [87*j, 486*j]], 1)

pg.display.flip()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
