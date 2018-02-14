import pygame
import sys

background = (0, 0, 0)
entity_color = (255, 255, 255)


class Entity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # This makes a rectangle around the entity, used for anything
        # from collision to moving around.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Paddle(Entity):
    """
    Player controlled or AI controlled, main interaction with
    the game
    """

    def __init__(self, x, y, width, height):
        super(Paddle, self).__init__(x, y, width, height)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(entity_color)


class Player(Paddle):
    """The player controlled Paddle"""

    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)

        # How many pixels the Player Paddle should move on a given frame.
        self.y_change = 0
        # How many pixels the paddle should move each frame a key is pressed.
        self.y_dist = 5

    def MoveKeyDown(self, key):
        """Responds to a key-down event and moves accordingly"""
        if (key == pygame.K_UP):
            self.y_change += -self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += self.y_dist

    def MoveKeyUp(self, key):
        """Responds to a key-up event and stops movement accordingly"""
        if (key == pygame.K_UP):
            self.y_change += self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += -self.y_dist

    def update(self):
        """
        Moves the paddle while ensuring it stays in bounds
        """
        # Moves it relative to its current location.
        self.rect.move_ip(0, self.y_change)

        # If the paddle moves off the screen, put it back on.
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > window_height - self.height:
            self.rect.y = window_height - self.height


class Enemy(Paddle):
    """
    AI controlled paddle, simply moves towards the ball
    and nothing else.
    """

    def __init__(self, x, y, width, height):
        super(Enemy, self).__init__(x, y, width, height)

        self.y_change = 4

    def update(self):
        """
        Moves the Paddle while ensuring it stays in bounds
        """
        # Moves the Paddle up if the ball is above,
        # and down if below.
        if ball.rect.y < self.rect.y:
            self.rect.y -= self.y_change
        elif ball.rect.y > self.rect.y:
            self.rect.y += self.y_change

        # The paddle can never go above the window since it follows
        # the ball, but this keeps it from going under.
        if self.rect.y + self.height > window_height:
            self.rect.y = window_height - self.height


class Ball(Entity):
    """
    The ball!  Moves around the screen.
    """

    def __init__(self, x, y, width, height):
        super(Ball, self).__init__(x, y, width, height)

        self.image = pygame.Surface([width, height])
        self.image.fill(entity_color)

        self.x_direction = 1
        # Positive = down, negative = up
        self.y_direction = 1
        # Current speed.
        self.speed = 3

    def update(self):
        # Move the ball!
        self.rect.move_ip(self.speed * self.x_direction,
                          self.speed * self.y_direction)

        # Keep the ball in bounds, and make it bounce off the sides.
        if self.rect.y < 0:
            self.y_direction *= -1
        elif self.rect.y > window_height - 20:
            self.y_direction *= -1
        if self.rect.x < 0:
            self.x_direction *= -1
        elif self.rect.x > window_width - 20:
            self.x_direction *= -1


pygame.init()

window_width = 700
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball = Ball(window_width / 2, window_height / 2, 20, 20)
player = Player(20, window_height / 2, 20, 50)
enemy = Enemy(window_width - 40, window_height / 2, 20, 50)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)
all_sprites_list.add(player)
all_sprites_list.add(enemy)

while True:
    # Event processing here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            player.MoveKeyDown(event.key)
        elif event.type == pygame.KEYUP:
            player.MoveKeyUp(event.key)

    for ent in all_sprites_list:
        ent.update()

    screen.fill(background)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)