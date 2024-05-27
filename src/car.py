import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class Car:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def move(self, dx=0, dy=0):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Limitar el movimiento dentro de la ventana
        self.rect.x = max(0, min(WINDOW_WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(WINDOW_HEIGHT - self.rect.height, self.rect.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)