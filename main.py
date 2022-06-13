import pygame
from time import sleep
pygame.init()
screen = pygame.display.set_mode((300,300))

# draw a green box
x = 10
y = 10
vx = 1
vy = 2

while True:
  pygame.draw.rect(screen, (100,100,100),   (0,0,300,300))
  pygame.draw.rect(screen, (0,255,0), (x, y, 100, 100))
  pygame.display.flip()
  x = x + vx  
  y = y + vy
  if x + 100 > 300: 
    vx = -0.8*vx
    x = 300-100
  if x < 0: 
    vx = -0.8*vx
    x = 0
  sleep(0.01)
  if y + 100 > 300: 
    vy = -vx
    y = 199
  if y < 0: 
    vy = -0.8*vx
    y = 0

  vx += 0.1
    
