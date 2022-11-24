import pygame
from world import World

# init la game
pygame.init()


# Variables
running = True
clock = pygame.time.Clock()
size = (800,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game of Life')

world = World(100, 3, 4,2, screen)
world.populateWorld()
while running:
    
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = True
    
    world.displayWorld(size)
    
    world.checkCell()
    
    
    
    pygame.display.flip()
    
    
    # l'horloge
    clock.tick(2)