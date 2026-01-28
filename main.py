import pygame as pg
import random
from bird import Bird
from pipe import Pipe

pg.init()

VINDU_BREDDE = 600
VINDU_HOYDE = 600

font = pg.font.SysFont('Impact', 24)



score = font.render("1", True, "black")
score_rect = score.get_rect(center=(VINDU_BREDDE/2, 50))

vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
klokke = pg.time.Clock()
fps = 60
fortsett = True

bird = Bird(75, VINDU_BREDDE/2-20, 20, 20, 0, 0.5, 10)

pipes = []
last_spawn = pg.time.get_ticks()
spawn_frequency = 1500

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bird.jump()

    time_now = pg.time.get_ticks()
    if time_now - last_spawn > spawn_frequency:
        height = random.randint(50, 400)
        top_pipe = Pipe(600, 0, 50, height, 3)
        bottom_pipe = Pipe(600, height + 150, 50, 600 - height - 150, 3)
        pipes.extend([top_pipe, bottom_pipe])
        last_spawn = time_now



    vindu.fill((0, 0, 0))

    for pipe in pipes:
        pipe.update()
        pipe.draw(vindu)
    
    active_pipes = []
    for pipe in pipes:
        if pipe.rect.right > 0:
            active_pipes.append(pipe)
    
    pipes = active_pipes

    bird.update()
    bird.draw(vindu)

    bird.check_collision(pipes)

    pg.display.update()
    klokke.tick(fps)

pg.quit()
