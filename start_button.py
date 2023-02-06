import pygame

#Button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        #Once mouse collides with button & is clicked set clicked and action to True.
        if self.rect.collidepoint(pos):
            #right click on mouse is True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                self.rect
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draws button png on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action