import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DINO_START, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.death_count = 0

        self.executing = False

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        # poner color al fondo
        self.screen.fill((255, 255, 255))

        # mostrar mensaje de inicio
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            font = pygame.font.Font(FONT_STYLE, 30)
            message = font.render("Press any key to Start", True, (0, 0, 0))
            message_rect = message.get_rect()
            message_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(message, message_rect)
        else:
            
            # mostrar puntos obtenidos
            font = pygame.font.Font(FONT_STYLE, 30)
            message = font.render(f"Your Score: " + {self.current_score}, True, (0, 0, 0))
            message_rect = message.get_rect()
            message_rect.center = (half_screen_width, half_screen_height + 50)
            self.screen.blit(message, message_rect)
            #mostrar mensaje de reinico
            font = pygame.font.Font(FONT_STYLE, 30)
            message = font.render("Press any key to Resstart", True, (0, 0, 0))
            message_rect = message.get_rect()
            message_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(message, message_rect)
            #mostrar muertes totales
            font = pygame.font.Font(FONT_STYLE, 30)
            message = font.render("You death: ", True, (0, 0, 0))
            message_rect = message.get_rect()
            message_rect.center = (half_screen_width, half_screen_height + 100)
            self.screen.blit(message, message_rect)
            print(self.death_count)
            
        # mostrar images como icono
        self.screen.blit(DINO_START, (half_screen_width - 20, half_screen_height - 140))
        # actualizar eventos
        pygame.display.flip()
        # manejar eventos
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
