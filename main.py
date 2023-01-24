import pygame
import random

pygame.init()
pygame.display.init()


# Set the size of the grid
grid_size = (20, 20)
screen_size = (600, 600)
fps = 60


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
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()
# Main loop
running = True
while running:
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

    if running:
        pygame.display.flip()
    clock.tick(fps)
pygame.quit()

