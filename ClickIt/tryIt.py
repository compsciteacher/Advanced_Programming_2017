import sys

import pygame as pg


class Mover(pg.sprite.Sprite):
    def __init__(self):
        super(Mover, self).__init__()
        self.image = pg.Surface((64, 64))
        self.image.fill(pg.Color("dodgerblue"))
        self.rect = self.image.get_rect(center=(100, 100))
        self.move_keys = {
                pg.K_a: (-1, 0),
                pg.K_d: (1, 0),
                pg.K_w: (0, -1),
                pg.K_s: (0, 1)}

    def update(self, pressed):
        for k in self.move_keys:
            if pressed[k]:
                self.rect.move_ip(self.move_keys[k])
                print('hmmm')
        if pressed[pg.K_i]:
            print('i')

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Game(object):
    def __init__(self, screen_size):
        self.done = False
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()
        self.fps = 60
        self.bg_color = pg.Color("gray5")
        self.mover = Mover()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def update(self, dt):
        pressed = pg.key.get_pressed()
        self.mover.update(pressed)

    def draw(self):
        self.screen.fill(self.bg_color)
        self.mover.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()


if __name__ == "__main__":
    game = Game((1280, 720))
    game.run()
    pg.quit()
    sys.exit()