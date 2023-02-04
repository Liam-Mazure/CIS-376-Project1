import pygame
import random

from Player import Player
from Fps_Slider import Fps_Slider
from Grid_Update import Grid_Update
import start_button

pygame.init()
pygame.display.init()
pygame.display.set_caption("CIS_376_Project1")


# Set the size of the grid
grid_size = (20, 20)
screen_size = (900, 600)
screen = pygame.display.set_mode(screen_size)

#Initialize player
player = Player(10, 10)

slider = Fps_Slider(650, 350, 30, 120)
sliders = pygame.sprite.Group()
sliders.add(slider)

fps = slider.value

font = pygame.font.Font(None, 30)

#load start button
start_pic = pygame.image.load('start_btn_orange.png').convert_alpha()

#Initialize start_btn
start_btn = start_button.Button(((900/2) - 130), ((600/2) - 70), start_pic)

buttonArea = pygame.Rect(600, 0, 300, 600)

# Get the size of each cell
cell_size = ((screen_size[0] - buttonArea.width) // grid_size[0], screen_size[1] // grid_size[1])

# Create an empty grid
grid = [[random.randint(0, 1) for x in range(grid_size[0])] for y in range(grid_size[1])]

# Create a cell sprite for each cell in the grid
for x in range(grid_size[0]):
    for y in range(grid_size[1]):
        cell = pygame.sprite.Sprite()
        cell.rect = pygame.Rect(x*cell_size[0], y*cell_size[1], cell_size[0], cell_size[1])
        cell.alive = grid[x][y]
        grid[x][y] = cell

clock = pygame.time.Clock()

def intro_screen():
    intro = True
    start = False

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill("black")
        if start_btn.draw(screen):
            print("Start")
            start = True 
            intro = False
        pygame.display.update()
    return start

# Main loop
def game_loop():
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
                if x >= 0 and x < grid_size[0] and y >= 0 and y < grid_size[1]:
                    grid[x][y].alive = not grid[x][y].alive
            Grid_Update.update_grid(grid_size, grid, fps)

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
            pygame.draw.rect(screen, (255, 255, 255), buttonArea)

        if running:
            mouse_pos = pygame.mouse.get_pos()
            sliders.update(mouse_pos)
            sliders.draw(screen)
            fps_text = font.render("FPS: {:.2f}".format(slider.value), True, (0,0, 0))
            screen.blit(fps_text, (650, 325))

            pygame.display.update()

        if running:
            player.update_player(cell_size, grid)
            pygame.display.flip()
        clock.tick(fps)

intro_screen()
if intro_screen:
    game_loop()
pygame.quit()
