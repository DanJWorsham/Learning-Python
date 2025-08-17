import pygame as pg

pg.display.init()
screen = pg.display.set_mode((200,200))
pg.display.flip()

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False