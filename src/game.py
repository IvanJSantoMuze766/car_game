import pygame
import random
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BLACK
from car import Car
from obstacle import Obstacle
import utils


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Car Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.car = Car("assets/images/car.png", WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100)
        self.obstacles = []
        self.spawn_obstacle()

    def spawn_obstacle(self):
        # Generar una posición aleatoria en el eje x dentro del ancho de la ventana
        x_position = random.randint(0, WINDOW_WIDTH - 50)  # Ajusta 50 al tamaño del obstáculo
        obstacle = Obstacle("assets/images/obstacle.png", x_position, -100, 5)
        self.obstacles.append(obstacle)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.car.move(dx=-1)
        if keys[pygame.K_RIGHT]:
            self.car.move(dx=1)
        if keys[pygame.K_UP]:
            self.car.move(dy=-1)
        if keys[pygame.K_DOWN]:
            self.car.move(dy=1)

        for obstacle in self.obstacles:
            obstacle.move()
            if obstacle.is_off_screen():
                self.obstacles.remove(obstacle)
                self.spawn_obstacle()
            # Verificar colisiones
            if self.car.rect.colliderect(obstacle.rect):
                self.running = False  # Detener el juego si hay una colisión

    def draw(self):
        self.screen.fill(BLACK)
        self.car.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        pygame.display.flip()

    def show_game_over(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Esperar 2 segundos antes de salir

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.show_game_over()
        pygame.quit()