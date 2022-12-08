from pygame import Surface

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, images: list[Surface]):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.images[self.index//5], self.rect)
        self.index += 1
