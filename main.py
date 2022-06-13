from lib2to3.pgen2.pgen import ParserGenerator
from telnetlib import XASCII
import pygame
from time import sleep

pygame.init()

screen_x = 500
screen_y = 500
box_width = 100
box_height = 50

screen = pygame.display.set_mode((screen_x, screen_y))

tick_time = 0.01

# draw a green box
x = 10
y = 10
vx = 1
vy = 2
ddx = 0.1
ddy = 0.1
x_target = 100
y_target = 100
target_h = 10
target_w = 10
target_vx = 0
target_vy = 0


def render():
    global x, y, x_target, y_target, target_w, target_h
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, screen_x, screen_y))
    pygame.draw.rect(screen, (0, 255, 0), (x, y, box_width, box_height))
    if rect_in_rect(x_target, y_target, target_w, target_h, x, y, box_width,
                    box_height):
        target_color = (255, 0, 0)
    else:
        target_color = (0, 0, 255)
    pygame.draw.rect(screen, target_color,
                     (x_target, y_target, target_w, target_h))

    pygame.display.flip()


def point_in_rect(x, y, xr, yr, w, h):
    return xr < x < xr + w and yr < y < yr + h


def rect_in_rect(x1, y1, w1, h1, x2, y2, w2, h2):
    return point_in_rect(x1, y1, x2, y2, w2, h2) and \
           point_in_rect(x1+w1, y1+h1, x2, y2, w2, h2)


def state_update():
    global x, y, vx, vy, ddx, ddy, x_target, y_target, target_vx, target_vy,\
           box_width, box_height
    x = x + vx
    y = y + vy
    if x + box_width > screen_x:
        vx = -0.8 * vx
        x = screen_x - box_width
    if x < 0:
        vx = -0.8 * vx
        x = 0

    if y + box_height > screen_y:
        vy = -0.8 * vy
        y = screen_y - box_height
    if y < 0:
        vy = -0.8 * vy
        y = 0

    x_target += target_vx
    y_target += target_vy

    #vy += 0.1
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vx -= ddx
    if keys[pygame.K_RIGHT]:
        vx += ddx
    if keys[pygame.K_UP]:
        vy -= ddy
    if keys[pygame.K_DOWN]:
        vy += ddy

    if keys[pygame.K_SPACE]:
      if rect_in_rect(x_target, y_target, target_w, 
                        target_h, x, y, box_width,
                        box_height):
        print("hit!")
      else:
        print("miss!")


    if x_target + target_w > screen_x:
        target_vx *= -1
    if x_target < 0:
        target_vx *= -1
    if y_target + target_h > screen_y:
        target_vy *= -1
    if y_target < 0:
        target_vy *= -1

    


def tick():
    state_update()
    render()
    sleep(tick_time)


while True:
    tick()
