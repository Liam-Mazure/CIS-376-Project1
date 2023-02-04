import pygame

class Grid_Update():

    last_update = pygame.time.get_ticks()

    def update_grid(grid_size=None, grid=None, fps=None):
        # Iterate through each cell in the grid
        # Get the current time
        current_time = pygame.time.get_ticks()

        if current_time - Grid_Update.last_update >= 10000 / fps:
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
            Grid_Update.last_update = current_time