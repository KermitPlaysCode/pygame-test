#
# Credits to https://www.youtube.com/watch?v=AY9MnQ4x3zk
# Source of almost


import pygame
from sys import exit
from os.path import dirname

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("dam it works")
clock = pygame.time.Clock()

test_surface = pygame.Surface((20,20))
test_surface.fill('Blue')

bg_surface = pygame.Surface((20,20))
test_surface.fill('White')

lastx = 100
lasty = 100

varx = 4
vary = -1
minx = 10
maxx = 790
miny = 255
maxy = 265

x=minx
y=miny

base_directory = dirname(__file__)
bg_surface = pygame.image.load(f'{base_directory}/bg.jpg')
boat_surface = pygame.image.load(f'{base_directory}/boat.png')
boat_rect = boat_surface.get_rect(midtop=(x,y))
my_font = pygame.font.Font(None, 48)
text_surface = my_font.render('Mon bateau', 'False', 'white')
txt_srf = my_font.render('BOUM', 'False', 'red')
t = 0
flag_boum = False
flag_clic = False
fps = 30

iwannastay = True
while iwannastay:
    # Enven loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            iwannastay = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag_clic = True

    # In order drawing: back to front (like stacking them)
    screen.blit(bg_surface, (0,0))
    screen.blit(text_surface, (100,100))
    screen.blit(boat_surface, boat_rect)
    boat_rect.top += vary
    y += vary
    if y > maxy or y < miny:
        vary = -vary
    boat_rect.right += varx
    x += varx
    if x > maxx:
        x = minx
        boat_rect.right = minx
    
    # Mouse position, collision with a rect
    mouse_pos = pygame.mouse.get_pos()
    t += 1
    if t > fps:
        flag_boum = False
        t = 0
    if flag_clic and boat_rect.collidepoint(mouse_pos):
        t = 0
        boum_pos = (mouse_pos[0] + 10, mouse_pos[1]+10) 
        flag_boum = True
    flag_clic = False
    if flag_boum:
        txt_rect = txt_srf.get_rect(topleft = boum_pos)
        pygame.draw.rect(screen, 'yellow', txt_rect, border_radius = 10)
        screen.blit(txt_srf, boum_pos)

    # Draw !
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
