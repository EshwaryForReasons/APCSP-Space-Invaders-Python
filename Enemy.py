import pygame

class AEnemy:
    def __init__(self, _game, _x, _y):
        self.x = _x
        self.y = _y
        self.game = _game
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.game.screen, (200, 200, 200), pygame.Rect(self.x, self.y, self.size, self.size))

    def checkCollision(self, game):
        for rocket in game.Rockets:
            if rocket.x < self.x + self.size and rocket.x > self.x - self.size and rocket.y < self.y + self.size and rocket.y > self.y - self.size:
                game.Rockets.remove(rocket)
                game.Enemies.remove(self)