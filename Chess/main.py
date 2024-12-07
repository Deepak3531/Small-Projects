# two player of chess game in python with pygame!
# set up variable, images and game loop

import pygame

pygame.init()
width = 1000
height = 900
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Two-player pygame chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game variable and images


# game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark grey')
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()
        