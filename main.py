import pygame as pg
import random
from bird import Bird
from pipe import Pipe

pg.init()

VINDU_BREDDE = 600
VINDU_HOYDE = 600

vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
klokke = pg.time.Clock()
fps = 60
fortsett = True

bird = Bird(75, VINDU_BREDDE/2-20, 20, 20, 0, 0.5, 10)
score = 0
font = pg.font.SysFont('Impact', 24)
font_gameover = pg.font.SysFont('Impact', 60)
font_start = pg.font.SysFont('Impact', 40)

pipes = []
last_spawn = pg.time.get_ticks()
spawn_frequency = 1500
game_state = "start"

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        
        if (event.type == pg.KEYDOWN and event.key == pg.K_SPACE) or event.type == pg.MOUSEBUTTONDOWN:
            if game_state == "start":
                game_state = "playing"
                bird.jump()
            elif game_state == "playing":
                bird.jump()
            elif game_state == "game_over":
                bird = Bird(75, VINDU_BREDDE/2-20, 20, 20, 0, 0.5, 10)
                pipes = []
                score = 0
                game_state = "start"
                last_spawn = pg.time.get_ticks()

    vindu.fill((135, 206, 250))

    if game_state == "playing":
        time_now = pg.time.get_ticks()
        if time_now - last_spawn > spawn_frequency:
            height = random.randint(50, 400)
            top_pipe = Pipe(600, 0, 140, height, 3, flip=True)
            bottom_pipe = Pipe(600, height + 150, 140, 600 - height - 150, 3)
            pipes.extend([top_pipe, bottom_pipe])
            last_spawn = time_now

        for pipe in pipes:
            pipe.update()

            if not pipe.passed and (pipe.rect.right - 44) < bird.rect.left:
                pipe.passed = True
                if pipe.rect.top == 0:
                    score += 1
        
        active_pipes = [] 
        for pipe in pipes:
            if pipe.rect.right > 0:
                active_pipes.append(pipe)
        pipes = active_pipes

        bird.update()
        bird.check_collision(pipes, VINDU_HOYDE)
        
        if bird._gravity == 0:
            game_state = "game_over"

    for pipe in pipes:
        pipe.draw(vindu)

    bird.draw(vindu)
    
    score_text = font.render(str(score), True, "white")
    score_rect = score_text.get_rect(center=(VINDU_BREDDE/2, 50))
    vindu.blit(score_text, score_rect)

    if game_state == "start":
        start_text = font_start.render("Tap or Press SPACE", True, "white")
        start_rect = start_text.get_rect(center=(VINDU_BREDDE/2, VINDU_HOYDE/2))
        vindu.blit(start_text, start_rect)
    
    if game_state == "game_over":
        game_over_text = font_gameover.render("GAME OVER", True, "red")
        game_over_rect = game_over_text.get_rect(center=(VINDU_BREDDE/2, VINDU_HOYDE/2))
        vindu.blit(game_over_text, game_over_rect)

    pg.display.update()
    klokke.tick(fps)

pg.quit()
