import pygame
import pygame_gui
import random
import math

WIDTH = 1280
HEIGHT = 720

#-------------Setup-------------
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 25)

gui_manager = pygame_gui.UIManager((WIDTH,HEIGHT))
clock = pygame.time.Clock()
                
while running:
    time_delta = clock.tick(60)/1000.0
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
        gui_manager.process_events(event)
    gui_manager.update(time_delta)
    gui_manager.draw_ui(screen)
            
    screen.fill("gray")

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()