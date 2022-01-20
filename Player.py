import pygame

class APlayer():
    def __init__(self, _game, _x, _y):
        self.x = _x
        self.y = _y
        self.game = _game

    def draw(self):
        pygame.draw.rect(self.game.screen, (200, 200, 200), pygame.Rect(self.x, self.y, 20, 20))