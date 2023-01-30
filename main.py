import pygame
import random
import start_button

pygame.init()
pygame.display.init()
pygame.display.set_caption("CIS_376_Project1")

# Set the size of the grid
grid_size = (20, 20)
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
fps = 60

#load start button
start_pic = pygame.image.load('start_btn_orange.png').convert_alpha()

# Get the size of each cell
cell_size = (screen_size[0] // grid_size[0], screen_size[1] // grid_size[1])

# Create an empty grid
grid = [[random.randint(0, 1) for x in range(grid_size[0])] for y in range(grid_size[1])]

# Create a cell sprite for each cell in the grid
for x in range(grid_size[0]):
    for y in range(grid_size[1]):
        cell = pygame.sprite.Sprite()
        cell.rect = pygame.Rect(x*cell_size[0], y*cell_size[1], cell_size[0], cell_size[1])
        cell.alive = grid[x][y]
        grid[x][y] = cell

def update_grid():
    # Iterate through each cell in the grid
    # Get the current time
    current_time = pygame.time.get_ticks()
    if current_time - update_grid.last_update >= 10000 / fps:
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                # Check the number of alive neighbors
                alive_neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (0 <= x+i < grid_size[0]) and (0 <= y+j < grid_size[1]) and (i != 0 or j != 0):
                            if grid[x+i][y+j].alive:
                                alive_neighbors += 1
                # Update the cell's status based on the rules
                if grid[x][y].alive:
                    if alive_neighbors < 1 or alive_neighbors > 4:
                        grid[x][y].alive = False
                else:
                    if alive_neighbors == 3:
                        grid[x][y].alive = True
        update_grid.last_update = current_time

update_grid.last_update = pygame.time.get_ticks()

clock = pygame.time.Clock()

#Player class
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
        pygame.draw.rect(screen, self.color, self.rect)

    def update_player(self):
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


#Initialize start_btn
start_btn = start_button.Button((600/2), (600/2), start_pic)

#Initialize player
player = Player(10,10)

# Main loop
running = True
while running:

    if start_btn.draw(screen):
        print("Start")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Check which cell was clicked
            x, y = pos[0] // cell_size[0], pos[1] // cell_size[1]
            grid[x][y].alive = not grid[x][y].alive
        update_grid()

        #Check if arrow keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left = True
            if event.key == pygame.K_RIGHT:
                player.right = True
            if event.key == pygame.K_UP:
                player.up = True
            if event.key == pygame.K_DOWN:
                player.down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left = False
            if event.key == pygame.K_RIGHT:
                player.right = False
            if event.key == pygame.K_UP:
                player.up = False
            if event.key == pygame.K_DOWN:
                player.down = False

    # Clear the screen
    if running:
        screen.fill((0, 0, 0))

    # Draw the grid
    if running:
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                color = (0, 255, 0) if grid[x][y].alive else (0, 0, 0)
                pygame.draw.rect(screen, color, grid[x][y].rect)
                pygame.draw.rect(screen, (0, 0, 0), grid[x][y].rect, 1)
            x = grid_size[0] - 1
            y = grid_size[1]-1
            grid[x][y].color = (255, 0, 0)
            pygame.draw.rect(screen, grid[x][y].color, grid[x][y].rect)
        player.draw(screen)
        if grid[grid_size[0] - 1][y].rect.colliderect(player.rect):
            running = False
            print("Game Over")


    if running:
        player.update_player()
        pygame.display.flip()
    clock.tick(fps)
pygame.quit()

