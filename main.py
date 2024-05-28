import pygame
from random import randrange
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard
import time


import sys
import os

pygame.init()
pygame.font.init()

paddle = Paddle()
ball = Ball()
blocks = Blocks()
scoreboard = Scoreboard()

WIDTH, HEIGHT = 1280, 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

dt = 0

BG_IMAGE_SIZE = (WIDTH, HEIGHT)
bg_img = pygame.image.load("space_photo.jpg").convert()
bg_img = pygame.transform.scale(bg_img, BG_IMAGE_SIZE)


def ball_blocks_collisions(dx,dy, ball, block):
    if dx > 0:
        delta_x = ball.right - block.left
    else:
        delta_x = block.right - ball.left

    if dy > 0:
        delta_y = ball.bottom - block.top
    else:
        delta_y = block.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy






running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ##provides the background image
    screen.blit(bg_img, (0, 0))

    ###initialise ball
    ball.draw_ball(screen)
    ball.ball_collision()

    ###initialise paddle
    paddle.draw_paddle(screen)
    paddle.move_paddle()

    ###initialise blocks
    blocks.draw_blocks(screen)
    scoreboard.write_score(screen)


    ###ball collision with paddle
    if ball.ball.colliderect(paddle.paddle) and ball.dy > 0:
        ball.dy = - ball.dy

    ### ball collision with blocks
    hit_index = ball.ball.collidelist(blocks.block_list)
    if hit_index != -1:
        hit_block = blocks.block_list.pop(hit_index)
        hit_colour = blocks.colour_list.pop(hit_index)
        ball.dx, ball.dy = ball_blocks_collisions(ball.dx, ball.dy, ball.ball, hit_block)
        ### special effects
        hit_block.inflate_ip(ball.ball.width * 3, ball.ball.height * 3)
        pygame.draw.rect(screen, hit_colour, hit_block)

        ### scoring conditions
        scoreboard.get_score(screen)


    #### GAME OVER situation
    #### need to reset things and then start ball moving again
    if ball.ball.bottom > HEIGHT:
        scoreboard.game_over(screen)
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            ball.draw_ball(screen)
            blocks.clear_blocks(screen)
            blocks.draw_blocks(screen)

            #time.sleep(2)




        #fps += 2   ###increase speed of game





    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

