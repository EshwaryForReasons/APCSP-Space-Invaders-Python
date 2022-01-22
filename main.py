import pygame
from Player import APlayer as APlayer
from Rocket import ARocket as ARocket
from Enemy import AEnemy as AEnemy

class Main():
    screen = None

    bIsWinner = False
    bIsLoser = False

    Wave = 0
    RocketsLeft = 30

    Enemies = []
    Rockets = []

    def __init__(self, _width, _height):
        pygame.init()
        self.width = _width
        self.height = _height
        self.screen = pygame.display.set_mode((_width, _height))
        self.clock = pygame.time.Clock()

        self.bKeepOpen = True

        self.Player = APlayer(self, _width/2, _height - 50) 
        self.Generator = Generator(self)

        self.StartGameLoop()

    def DisplayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (40, 0, 60))
        self.screen.blit(textsurface, (110, 160))

    def EndGameLoop(self):
        self.bKeepOpen = False
    
    def StartGameLoop(self):
        while self.bKeepOpen:
            #PyGame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.EndGameLoop()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.Rockets.append(ARocket(self, self.Player.x, self.Player.y))

            #Get left and right events to move the player
            Pressed = pygame.key.get_pressed()

            if Pressed[pygame.K_LEFT]:
                self.Player.x -= 2 if self.Player.x > 20 else 0
            elif Pressed[pygame.K_RIGHT]:
                self.Player.x += 2 if self.Player.x < self.width - 40 else 0

            #Update the screen every frame
            pygame.display.flip()
            self.clock.tick(144)
            self.screen.fill((0, 0, 0))

            #Show the enemies on screen every frame
            for Enemy in self.Enemies:
                Enemy.draw()
                Enemy.checkCollision(self)

                if(Enemy.y > self.height):
                    bIsLoser = True

            #Show the rockets on screen every frame
            for Rocket in self.Rockets:
                Rocket.Draw()

            #Show player on screen every frame
            self.Player.draw()

class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.Enemies.append(AEnemy(game, x, y))

main = Main(1000, 600)