import pygame
from time import sleep
pygame.init()

screen_x = 500
screen_y = 500
box_width = 100
box_height = 50

screen = pygame.display.set_mode((screen_x,screen_y))

tick_time = 0.01

# draw a green box
x = 10
y = 10
vx = 1
vy = 2


def render():
  global x,y
  pygame.draw.rect(screen, (100,100,100),   (0,0,screen_x,screen_y))
  pygame.draw.rect(screen, (0,255,0), (x, y, 
                                       box_width, box_height))
  pygame.display.flip()
  
def state_update():
  global x, y, vx, vy
  x = x + vx  
  y = y + vy
  if x + box_width > screen_x: 
    vx = -0.8*vx
    x = screen_x - box_width
  if x < 0: 
    vx = -0.8*vx
    x = 0
  
  if y + box_height > screen_y: 
    vy = -0.8*vy
    y = screen_y - box_height
  if y < 0: 
    vy = -0.8*vy
    y = 0
  
  vy += 0.1

def tick():
  state_update()
  render()
  sleep(tick_time)

while True:
  tick()
    
