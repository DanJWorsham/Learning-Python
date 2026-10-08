import pygame as pg

#Setup pygame screen
pg.display.init()
screen = pg.display.set_mode((200,200))
pg.display.flip()

#Initialize Font
pg.font.init()
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BASE_FONT_SIZE = 20
fontSize = BASE_FONT_SIZE
font = pg.font.SysFont(None, fontSize)

running = True

#Establish Count variables and event
COUNT_EVENT = pg.USEREVENT + 1
count_tick = True
count_current = 1
count_to = 10

# Running Loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
        if event.type == COUNT_EVENT:
            count_tick = True
    
    if count_tick == True:
        count_tick = False
        count_current += 1
        pg.time.set_timer(COUNT_EVENT,1000)

    if count_current > count_to:
        count_current = 1
    
    #Draw Number on screen
    screen.fill(BLACK)
    Text_Surface = font.render(str(count_current), True, WHITE)
    screen.blit(Text_Surface, Text_Surface.get_rect(center=(100,100)))
    pg.display.flip()