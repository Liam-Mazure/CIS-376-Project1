import pygame

# Player class
class Player:
     
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.color = (255, 255, 255)
        self.curX = 0
        self.curY = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.speed = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], 5, 0)

    def update_player(self, cell_size=None, grid=None):
        screenWidth = 600
        screenHeight = 600
        self.curX = 0
        self.curY = 0
        position = (self.x, self.y)
        grid_x, grid_y = position[0] // cell_size[0], position[1] // cell_size[1]

        if not grid[grid_x][grid_y].alive:
            if self.left and not self.right:
                self.curX = -self.speed
            if self.right and not self.left:
                self.curX = self.speed
            if self.up and not self.down:
                self.curY = -self.speed
            if self.down and not self.up:
                self.curY = self.speed

            self.x += self.curX
            if self.x < 0:
                self.x = 0
            elif self.x > screenWidth - self.rect.width:
                self.x = screenWidth - self.rect.width
            self.y += self.curY
            if self.y < 0:
                self.y = 0
            elif self.y > screenHeight - self.rect.height:
                self.y = screenHeight - self.rect.height
            self.rect = pygame.Rect(int(self.x), int(self.y), 10, 10)