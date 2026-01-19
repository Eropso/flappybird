import pygame as pg

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

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False



    vindu.fill((0, 0, 0))



    pg.display.update()
    klokke.tick(fps)

pg.quit()
