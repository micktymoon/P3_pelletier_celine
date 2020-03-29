import sys, pygame
import random
pygame.init()

# Screen creation:
screen = pygame.display.set_mode((300, 300))


class Player(pygame.sprite.Sprite):
    """Class player."""

    def __init__(self, departure):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('MacGyver.png').convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.speed_right = [20, 0]
        self.speed_left = [-20, 0]
        self.speed_up = [0, -20]
        self.speed_down = [0, 20]
        self.pos = self.rect.move(departure)
        self.obj1 = False
        self.obj2 = False

    def move_right(self):
        """move the player on the right."""

        self.pos = self.pos.move(self.speed_right)
        if self.pos.right > 280:
            self.pos.right = 260

    def move_left(self):
        """move the player on the left."""

        self.pos = self.pos.move(self.speed_left)
        if self.pos.left < 0:
            self.pos.left = 40

    def move_up(self):
        """move the player on the top."""

        self.pos = self.pos.move(self.speed_up)
        if self.pos.top < 0:
            self.pos.top = 40

    def move_down(self):
        """move the player on the bottom."""

        self.pos = self.pos.move(self.speed_down)
        if self.pos.bottom > 280:
            self.pos.bottom = 260

    def draw_me(self):
        """draw player."""

        screen.blit(self.image, self.pos, self.rect)


class Labobject(pygame.sprite.Sprite):
    """Class for labyrinth objects."""

    def __init__(self, image, list):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos = random.choice(list)

    def draw_me(self):
        """draw object on the screen."""
        return screen.blit(self.image, self.pos, self.rect)

    def erase_me(self):
        """clears the object on the screen."""
        self.image.fill((0, 0, 0, 0))


class Guardian(pygame.sprite.Sprite):
    """Class for the labyrinth guardian."""
    def __init__(self, arrival):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Gardien.png').convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos = self.rect.move(arrival)

    def draw_me(self):
        """draw guardian on the screen."""
        return screen.blit(self.image, self.pos, self.rect)

    def erase_me(self):
        """clears the guardian on the screen."""
        self.image.fill((0, 0, 0, 0))
