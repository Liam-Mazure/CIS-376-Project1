import pygame
from pygame.sprite import Sprite


class Fps_Slider(Sprite):
    def __init__(self, x, y, minFps, maxFps):
        super().__init__()
        self.image = pygame.Surface((200, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.minFps = minFps
        self.maxFps = maxFps
        self.value = 60
        self.is_clicked = False

    def update(self, mouse_pos):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_pos):
            self.is_clicked = True
        elif pygame.mouse.get_pressed()[0] == False:
            self.is_clicked = False
        if self.is_clicked:
            self.value = (mouse_pos[0] - self.rect.x) / self.rect.w * (self.maxFps - self.minFps) + self.minFps
            self.value = min(max(1, self.value),120)
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, self.value / self.maxFps * self.rect.w, self.rect.h), 0)
