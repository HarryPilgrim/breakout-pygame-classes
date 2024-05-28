import pygame
from random import randrange
WIDTH, HEIGHT = 1280, 720


class Ball:
    """make the ball and handle its movement"""

    def __init__(self):
        self.ball_radius = 20
        self.ball_speed = 5
        self.ball_rect = int(self.ball_radius * (2**0.5))
        self.dx = 1
        self.dy = -1



        self.ball = pygame.Rect(randrange(self.ball_rect, WIDTH - self.ball_rect), HEIGHT // 2, self.ball_rect, self.ball_rect)


    def draw_ball(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.ball.center, self.ball_radius)

        ##start the balls movement
        self.ball.x += self.ball_speed * self.dx
        self.ball.y += self.ball_speed * self.dy

    def ball_collision(self):
        ##left to right walls
        if self.ball.centerx < self.ball_radius or self.ball.centerx > WIDTH - self.ball_radius:
            self.dx = -self.dx

        # ##top and bottom walls
        # if self.ball.centery < self.ball_radius or self.ball.centery > HEIGHT - self.ball_radius:
        #     self.dy = -self.dy

        #### top wall
        if self.ball.centery < self.ball_radius:
            self.dy = -self.dy

