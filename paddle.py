import pygame
WIDTH, HEIGHT = 1280, 720


class Paddle:
    """initialise the paddle and its movement"""

    def __init__(self):
        self.paddle_width = 300
        self.paddle_height = 30
        self.paddle_speed = 15
        self.paddle = pygame.Rect(WIDTH // 2 - self.paddle_width //2, HEIGHT - self.paddle_height - 25, self.paddle_width, self.paddle_height)


    def draw_paddle(self, screen):
        pygame.draw.rect(screen, pygame.Color("darkgreen"), self.paddle)


    def move_paddle(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.paddle.left > 0:
            self.paddle.left -= self.paddle_speed


        if key[pygame.K_RIGHT] and self.paddle.right < WIDTH:
            self.paddle.right += self.paddle_speed


