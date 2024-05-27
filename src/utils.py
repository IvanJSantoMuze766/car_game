import pygame

def load_image(file_path):
    return pygame.image.load(file_path)

def load_sound(file_path):
    return pygame.mixer.Sound(file_path)