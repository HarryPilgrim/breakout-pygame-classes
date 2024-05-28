import pygame
from random import randrange
import sys
import os

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 1280, 720

class Scoreboard:
    """displaying the score and level on screen, and game over situation"""

    def __init__(self):
        self.score = 0
        self.score_increment = 10
        self.level = 1
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def game_over(self, screen):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

            self.write_score(screen)
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER. press space bar to play again", True, (200, 200, 255))
        screen.blit(game_over_text, (WIDTH / 5, HEIGHT / 2))

        self.score = 0
        self.level = 1



    def write_score(self, screen):
        font = pygame.font.Font(None, 36)

        level_text = font.render(f'level: {self.level}', True, (255, 255, 255))
        screen.blit(level_text, (10, HEIGHT - 40))

        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, HEIGHT - 70))

        high_score_text = font.render(f'high score: {self.high_score}', True, (255, 255, 255))
        screen.blit(high_score_text, (10, HEIGHT - 100))


    def get_score(self, screen):

        self.score += self.score_increment
        self.write_score(screen)




