import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [-x+1600, 0])
        screen.blit(bg_img,[-x+3200, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        x += 1
        if x == 3200:
            x = 0
        clock.tick(200)
        key_lst = pg.key.get_pressed()
        x1 = -1
        y1 = 0
        if key_lst[pg.K_UP]:
            y1 = -1
        if key_lst[pg.K_DOWN]:
            y1 = 1
        if key_lst[pg.K_RIGHT]:
            x1 = 1
        if key_lst[pg.K_LEFT]:
            x1 = -1
        kk_rct.move_ip((x1, y1))

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()