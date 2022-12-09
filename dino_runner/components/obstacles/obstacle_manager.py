import pygame
from random import randint
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus, Cactus_1
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if randint(0, 2) == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif randint(0, 2) == 1:
                self.obstacles.append(Cactus_1(SMALL_CACTUS))
            elif randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if not game.player.shield:
                if game.player.dino_rect.colliderect(obstacle.rect):
                    if game.player.hammer:
                        self.obstacles.pop()
                    else:
                        game.player_heart_manager.reduce_heart_count()
                        if game.player_heart_manager.heart_count > 0:
                            self.obstacles.pop()
                        else: 
                            pygame.time.delay(500)
                            game.playing = False
                            game.death_count += 1        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
