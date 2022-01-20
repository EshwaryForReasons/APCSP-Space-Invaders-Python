import pygame
from Player import APlayer as APlayer
from Rocket import ARocket as ARocket

class Main():
    screen = None

    bIsWinner = False
    bIsLoser = False

    Wave = 0
    RocketsLeft = 30

    Aliens = []
    Rockets = []

    def __init__(self, _height, _width):
        pygame.init()
        self.width = _width
        self.height = _height
        self.screen = pygame.display.set_mode((_width, _height))
        self.clock = pygame.time.Clock()

        self.bKeepOpen = True

        self.Player = APlayer(self, _width/2, _height - 50)

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
                #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                   # self.Rockets.append(ARocket(self, self.Player.x, self.Player.y))

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

            #Show the rockets on screen every frame
            for Rocket in self.Rockets:
                Rocket.Draw()

            #Show player on screen every frame
            self.Player.draw()

main = Main(600, 600)