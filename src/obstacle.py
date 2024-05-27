import pygame

class Obstacle:
    def __init__(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def is_off_screen(self):
        return self.rect.y > pygame.display.get_surface().get_height()