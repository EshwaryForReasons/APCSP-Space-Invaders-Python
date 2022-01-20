import pygame

class ARocket():
    def __init__(self, _game, _x, _y):
        self.x = _x
        self.y = _y
        self.game = _game

    def Draw(self):
        pygame.draw.rect(self.game.screen, (250, 50, 110), pygame.Rect(self.x, self.y, 2, 4))

        self.y -= 2